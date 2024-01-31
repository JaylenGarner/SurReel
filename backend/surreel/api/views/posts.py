from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ..models import Post
from ..serializers import PostSerializer

# View functions

"""
Route: '/'
- GET: Get all posts
- POST: Create a post
"""

@api_view(['GET', 'POST'])
@csrf_exempt
def post_list(request):

    if request.method == 'GET':
        return get_all_posts(request)

    elif request.method == 'POST':
        return create_post(request)


    """
    Route: '/<id>'
    - GET: Get a post
    - PATCH: Update a post
    - DELETE: Delete a post
    """

@api_view(['GET', 'PATCH', 'DELETE'])
@csrf_exempt
def post_details(request, pk):


    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
       return get_post(post)

    elif request.method == 'PATCH':
        return edit_post(request, post)

    elif request.method == 'DELETE':
        return delete_post(post)


#  Helper Functions

def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    data_dict = {'posts': serializer.data}

    return JsonResponse(data_dict)


def get_post(post):
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data)


def create_post(request):
    data = JSONParser().parse(request)
    serializer = PostSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return  JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


def delete_post(post):
    post.delete()
    return HttpResponse(status=204)


def edit_post(request, post):
    data = JSONParser().parse(request)
    serializer = PostSerializer(post, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return  JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)