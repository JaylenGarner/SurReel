
from django.contrib import admin
from .models import User, Post, Media, Like, Follow, Room, Message

# Register your models here.

@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at')

@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at', 'updated_at')

@admin.register(Media)
class MediaModel(admin.ModelAdmin):
    list_display = ('post', 'url')

@admin.register(Room)
class RoomModel(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Message)
class MessageModel(admin.ModelAdmin):
    list_display = ('room', 'sender', 'media_url', 'created_at')
