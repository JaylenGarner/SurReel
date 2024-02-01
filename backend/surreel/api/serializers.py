from rest_framework import serializers
from .models import User, Post, Media, Like, Follow, Room, Message

from .exceptions.base_exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'image']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'caption']


class MediaSerializer(serializers.ModelSerializer):

    def validate(self, data):

        #test
        # if True:
        #     raise ValidationError('No sir nofefeeft today')
        return data

    class Meta:
        model = Media
        fields = ['id', 'post', 'url']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']


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
