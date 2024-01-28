from django.contrib import admin
from django.urls import path, include
from writers import views

urlpatterns = [
    path('', views.WritersView.as_view(), name='writers'),
    path('<str:slug>', views.UserView.as_view(), name='userView'),

    path('profile/<str:slug>', views.ProfileView.as_view(), name='profileView'),
    path('edit-profile/<str:slug>', views.EditProfileView.as_view(), name='editProfile'),

    path('newblog/<str:slug>', views.NewBlogView.as_view(), name='newBlog'),
    path('edit-blog/<str:slug>', views.EditBlogView.as_view(), name='editBlog'),
    path('delete-blog/<str:slug>', views.DeleteBlogView.as_view(), name='deleteBlog')
]

