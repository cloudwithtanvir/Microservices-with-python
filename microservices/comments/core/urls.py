
from django.contrib import admin
from django.urls import path
from .views import CommentAPIView

urlpatterns = [
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view()),
    path('comments', CommentAPIView.as_view()),
    
]
