from django.shortcuts import render
from blog.models import Post
from .serializers import PostSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class PostViews(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers