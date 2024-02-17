from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Post
from ..serializers import PostSerializer
from .media import create_media


class PostList(APIView):
    # Currently returns all posts. Will change to return posts for a user's feed.
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        media_data = request.data.pop('media', None)

        if media_data == None or not media_data:
            return Response({"detail" : "You must provide at least one media file for your post."}, status=status.HTTP_400_BAD_REQUEST)

        post_serializer = PostSerializer(data=request.data)

        if post_serializer.is_valid():
            post_instance = post_serializer.save()

            media_creation_errors = create_media(media_data, post_instance.id)

            if media_creation_errors is not None:
                post_instance.delete()
                return Response(media_creation_errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(post_serializer.data, status=status.HTTP_201_CREATED)

        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):

    def get_object(self, id):
        post = get_object_or_404(Post, pk=id)
        return post


    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def patch(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# ''' /<user_id>/posts '''

# @api_view(['GET'])
@csrf_exempt
def user_posts(request, pk):
    posts = Post.objects.filter(user=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)




def delete_post(post):
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def edit_post(request, post):
    serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
