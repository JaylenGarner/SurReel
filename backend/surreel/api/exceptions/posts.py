from rest_framework.exceptions import APIException

class NoMediaForPost(APIException):
    status_code = 400
    default_detail = "You must attach at least one media file to your post. Please upload a photo or video and try again."
