from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile-detail'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
