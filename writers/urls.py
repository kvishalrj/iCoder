from django.contrib import admin
from django.urls import path, include
from writers import views

urlpatterns = [
    path('', views.writers, name='writers'),
    path('<str:slug>', views.userView, name='userView'),

    path('profile/<str:slug>', views.profileView, name='profileView'),
    path('edit-profile/<str:slug>', views.editProfile, name='editProfile'),
    path('profileUpdate/<str:slug>', views.profileUpdate, name='profileUpdate'),

    path('newblog/<str:slug>', views.newBlog, name='newBlog'),
    path('saveNewBlog/<str:slug>', views.saveNewBlog, name='saveNewBlog'),
    path('edit-blog/<str:slug>', views.editBlog, name='editBlog'),
    path('blogUpdate/<str:slug>', views.blogUpdate, name='blogUpdate'),
    path('delete-blog/<str:slug>', views.deleteBlog, name='deleteBlog')
]

