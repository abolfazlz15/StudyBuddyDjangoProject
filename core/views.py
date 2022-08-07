from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, View)

from .forms import MessageFrom
from .models import Message, Room, Topic


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.filter(status=True)
        context['topics'] = Topic.objects.all()
        context['messages'] = Message.objects.filter(status=True)

        # get number_of_rooms
        number_of_rooms = 0
        for i in context['topics']:
            room = i.rooms.count()
            number_of_rooms = number_of_rooms + room
        context['count_all_room'] = number_of_rooms
        return context


class CreateRoomView(CreateView):
    model = Room
    fields = ['topic', 'name', 'description']
    template_name = 'core/create_room.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class DeleteMessageView(DeleteView):
    model = Message
    success_url = reverse_lazy('core:home')


class TopicDetailView(View):
    def setup(self, request, *args, **kwargs):
        self.topic = get_object_or_404(Topic, id=kwargs['pk'])
        self.rooms = self.topic.rooms.filter(status=True)
        self.topics = Topic.objects.all()
        self.message = Message.objects.filter(status=True)
        return super().setup(request, *args, **kwargs)

    def get(self, request, *arge, **kwarge):
        rooms = self.rooms
        topics = self.topics
        message = self.message

        context = {
            'rooms': rooms,
            'topics': topics,
            'messages': message,

        }
        return render(request, 'core/home.html', context)


class TopicListView(ListView):
    model = Topic
    template_name = 'core/topics.html'
    context_object_name = 'topics'

    def get_queryset(self, *args, **kwargs):
        topics = super().get_queryset(*args, **kwargs)

        q = self.request.GET.get('q')
        if q:
            return Topic.objects.filter(name__icontains=q)
        return topics


class SearchRoomView(ListView):
    model = Room
    template_name = 'core/home.html'
    context_object_name = 'rooms'

    def get_queryset(self, *args, **kwargs):
        rooms = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            return Room.objects.filter(
                Q(topic__name__icontains=q) |
                Q(name__icontains=q) |
                Q(description__icontains=q)
            ).filter(status=True)
        return rooms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        context['messages'] = Message.objects.filter(status=True)
        return context


class RoomDetailView(View):
    message_form_class = MessageFrom

    def setup(self, request, *args, **kwargs):
        self.room = get_object_or_404(Room, id=kwargs['pk'], slug=kwargs['slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *arge, **kwarge):
        room = self.room
        messages = room.message.all()
        context = {
            'room': room,
            'messages': messages,
            'form': self.message_form_class
        }
        return render(request, 'core/room.html', context)

    def post(self, request, *args, **kwargs):
        form = self.message_form_class(request.POST)
        if form.is_valid(): 
            message = form.save(commit=False)
            message.user = request.user
            message.room = self.room
            self.room.participants.add(request.user) # for add new user to participants 
            message.save()
            return redirect('core:room-detail', self.room.id, self.room.slug)
