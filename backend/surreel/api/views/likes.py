from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Like
from ..serializers import LikeSerializer


class LikePost(APIView):

    def post(self, request, post_id):
        request.data['post'] = post_id
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnlikePost(APIView):

    def get_object(self, post_id, user_id):
        like = Like.objects.filter(post=post_id, user_id=user_id)
        return like

    def delete(self, request, post_id):
        user_id = request.data['user']
        like = self.get_object(post_id, user_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
