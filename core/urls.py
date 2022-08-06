from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('createroom', views.CreateRoomView.as_view(), name='create-room'),

    # topic URL
    path('topic/<int:pk>', views.TopicDetailView.as_view(), name='topic-detail'),
    path('topics', views.TopicsView.as_view(), name='topics'),

    # Message URL
    path('deletemesssge/<int:pk>', views.DeleteMessageView.as_view(), name='delete-message'),
]
