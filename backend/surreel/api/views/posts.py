from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Post
from ..serializers import PostSerializer
from .media import create_media



# View Functions #


''' / '''

@api_view(['GET', 'POST'])
@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        return get_all_posts()

    elif request.method == 'POST':
        return create_post(request)


''' /<post_id> '''

@api_view(['GET', 'PATCH', 'DELETE'])
@csrf_exempt
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
       return get_post_by_id(post)

    elif request.method == 'PATCH':
        return edit_post(request, post)

    elif request.method == 'DELETE':
        return delete_post(post)


''' /<user_id>/posts '''

@api_view(['GET'])
@csrf_exempt
def user_posts(request, pk):
    posts = Post.objects.filter(user=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Helper Functions #

def get_all_posts():
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_post_by_id(post):
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)


def create_post(request):
    media_data = request.data.pop('media', None)

    if media_data == None or not media_data:
        return Response({"detail" : "You must provide at least one media file for your post."}, status=status.HTTP_404_NOT_FOUND)

    post_serializer = PostSerializer(data=request.data)

    if post_serializer.is_valid():
        post_instance = post_serializer.save()

        media_creation_errors = create_media(media_data, post_instance.id)

        if media_creation_errors is not None:
            post_instance.delete()
            return Response(media_creation_errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(post_serializer.data, status=status.HTTP_201_CREATED)

    return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_post(post):
    post.delete()
    return JsonResponse({"detail": "The post has been deleted"}, status=status.HTTP_200_OK)


def edit_post(request, post):
    data = JSONParser().parse(request)
    post_serializer = PostSerializer(post, data=data, partial=True)

    if post_serializer.is_valid():
        post_serializer.save()
        return Response(post_serializer.data, status=status.HTTP_200_OK)

    return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
