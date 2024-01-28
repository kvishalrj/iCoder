from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [

    # API to post comment
    path('postComment', views.PostCommentView.as_view(), name='postComment'),

    path('', views.BlogHomeView.as_view(), name='blogHome'),
    path('<str:slug>', views.BlogPostView.as_view(), name='blogPost')
]