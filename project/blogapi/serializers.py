from rest_framework import serializers
from blog.models import Post, Comment
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'