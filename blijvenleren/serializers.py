from rest_framework import serializers
from .models import Resource, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    serializers.PrimaryKeyRelatedField(
        source='post',
        queryset=Resource.objects.all()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'resource', 'content', 'status', 'created_at')

class ResourceSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = ('id', 'title', 'content', 'url', 'author', 'created_at', 'updated_at', 'comments')