from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Like
from ..serializers import LikeSerializer
from rest_framework import generics
from rest_framework import mixins


class LikePost(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, post_id):
        request.data['post'] = post_id
        return self.create(request, post=post_id)


class UnlikePost(generics.GenericAPIView, mixins.DestroyModelMixin):
    serializer_class = LikeSerializer
    lookup_field = 'post_id'

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        user_id = self.request.data.get('user')
        return Like.objects.filter(post=post_id, user=user_id)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
