from .base_exceptions import BaseCustomException
from rest_framework import status


class MediaLimitExceeded(BaseCustomException):
    def __init__(self):
        detail = "You can only attach up to 10 media files to a single post. Please remove any excess files and try again"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
