from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('createroom', views.CreateRoomView.as_view(), name='create-room'),

    # Message URL
    path('deletemesssge/<int:pk>', views.DeleteMessageView.as_view(), name='delete-message'),
]
