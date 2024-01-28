
from django.contrib import admin
from .models import User, Post, Media, Like, Follow, Room, Message

# Register your models here.

@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at')


@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ('id', 'get_author_username', 'caption', 'created_at', 'updated_at')

    def get_author_username(self, obj):
        return obj.user.username

    get_author_username.short_description = 'User'


@admin.register(Media)
class MediaModel(admin.ModelAdmin):
    list_display = ('id', 'get_post_id', 'url')

    def get_post_id(self, obj):
        return obj.post.id

    get_post_id.short_description = 'Post'


@admin.register(Room)
class RoomModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')



@admin.register(Message)
class MessageModel(admin.ModelAdmin):
    list_display = ('id', 'get_room_id', 'sender', 'content', 'media_url', 'created_at')

    def get_room_id(self, obj):
        return obj.room.id

    get_room_id.short_description = 'Room'
