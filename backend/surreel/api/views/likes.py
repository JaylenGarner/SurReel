from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Like
from ..serializers import LikeSerializer


class LikeList(APIView):

    def post(self, request, post_id):
        request.data['post'] = post_id
        print('REQUEST', request.data)
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetails(APIView):

    def get_object(self, like_id):
        like = get_object_or_404(Like, pk=like_id)
        return like

    def delete(self, request, like_id):
        like = self.get_object(like_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
