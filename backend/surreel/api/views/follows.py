from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Follow
from ..serializers import FollowSerializer

# class FollowUser(APIView):

#     def post(self, request, user_id):
#         request.data['followed'] = user_id
#         serializer = FollowSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
