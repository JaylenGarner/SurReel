from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Post
from ..serializers import PostSerializer
from .media import create_media
from rest_framework import generics
from rest_framework import mixins


class PostList(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)


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


class PostDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, id):
        return self.retrieve(request, id)

    def patch(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class UserPosts(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, user_id):
        return self.list(request, user=user_id)
