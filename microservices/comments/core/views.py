from django.shortcuts import render
from rest_framework import request, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Comment
from core.serializer import CommentSerializer

class PostCommentAPIView(APIView):
    def get(Self, _, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments ,many=True)
        return Response(serializers.Serializer.data)

# Create your views here.
class CommentAPIView(APIView):
    def post(self , request ):
        serializer = CommentSerializer(data= request, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)