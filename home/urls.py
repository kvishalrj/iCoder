from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('search', views.SearchView.as_view(), name='search'),
    path('signup', views.SignupView.as_view(), name='handleSignup'),
    path('login', views.LoginView.as_view(), name='handleLogin'),
    path('logout', views.LogoutView.as_view(), name='handleLogout')
]

