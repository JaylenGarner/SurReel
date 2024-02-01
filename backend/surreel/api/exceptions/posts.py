from .base_exceptions import BaseCustomException
from rest_framework import status


class NoMediaForPost(BaseCustomException):
    def __init__(self):
        detail = "You must attach at least one media file to your post. Please upload a photo or video and try again."
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
