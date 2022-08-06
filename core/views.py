from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, View, ListView

from .models import Message, Room, Topic


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self,*args, **kwargs):
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
        self.rooms = self.topic.rooms.all()
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


class TopicsView(ListView):
    model = Topic
    template_name = 'core/topics.html'
    context_object_name = 'topics'

    def get_queryset(self, *args, **kwargs):
        topics = super().get_queryset(*args, **kwargs)
        
        q = self.request.GET.get('q')
        if q:
            return Topic.objects.filter(name__icontains=q)
        return topics
