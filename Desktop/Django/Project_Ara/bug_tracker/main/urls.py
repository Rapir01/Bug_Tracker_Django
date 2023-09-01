from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name ='home'),
    path('home/', views.home, name ='home'),
    path('register', views.user_register, name ='user_register'),
    path('login/', views.user_login, name ='user_login'),
    path('profile/', views.profile, name = 'profile'),
    path('update/', views.user_info_update, name = 'user_info_update'),

    ]