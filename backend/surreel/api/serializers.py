from rest_framework import serializers
from .models import User, Post, Media, Like, Follow, Room, Message
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'image']

    def to_representation(self, value):
        return {
            'id': value.id,
            'username': value.id,
            'email': value.email,
            'first_name': value.first_name,
            'last_name': value.last_name,
            'image': value.image
        }


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'post', 'url']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']

    def to_representation(self, value):
        data = super().to_representation(value)
        data['user'] = UserSerializer(value.user).data
        return data


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    media = MediaSerializer(many=True, read_only=True, required=False)
    likes = LikeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', 'media', 'likes']

    def to_representation(self, value):
        data = super().to_representation(value)
        data['user'] = UserSerializer(value.user).data
        return data


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'followed']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'participants', 'name']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'media_url']
