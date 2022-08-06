from django.views.generic import CreateView, TemplateView, View, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
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

