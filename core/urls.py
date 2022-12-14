from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    # room URL
    path('room/<int:pk>/<slug:slug>', views.RoomDetailView.as_view(), name='room-detail'),
    path('', views.HomeView.as_view(), name='home'),
    path('createroom', views.CreateRoomView.as_view(), name='create-room'),
    path('search/', views.SearchRoomView.as_view(), name='search-room'),
    path('deleteroom/<int:pk>', views.DeleteRoomView.as_view(), name='delete-room'),

    # topic URL
    path('topic/<int:pk>', views.TopicDetailView.as_view(), name='topic-detail'),
    path('topics', views.TopicListView.as_view(), name='topic'),
    path('topics/create', views.CreateTopicView.as_view(), name='create-topic'),

    # Message URL
    path('deletemesssge/<int:pk>', views.DeleteMessageView.as_view(), name='delete-message'),
]
