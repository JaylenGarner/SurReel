from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ..models import Post
from ..serializers import PostSerializer

# /

@csrf_exempt
def post_list(request):

    if request.method == 'GET':
        return get_all_posts(request)

    elif request.method == 'POST':
        return create_post(request)


def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    data_dict = {'posts': serializer.data}

    return JsonResponse(data_dict)


def create_post(request):
    data = JSONParser().parse(request)
    serializer = PostSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return  JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)

# /<post_id>

@csrf_exempt
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
       return get_post(post)

    elif request.method == 'PUT':
        return edit_post(request, post)

    elif request.method == 'DELETE':
        return delete_post(post)


def get_post(post):
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data)


def edit_post(request, post):
    data = JSONParser().parse(request)
    serializer = PostSerializer(post, data=data)

    if serializer.is_valid():
        serializer.save()
        return  JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)

def delete_post(post):
    post.delete()
    return HttpResponse(status=204)
