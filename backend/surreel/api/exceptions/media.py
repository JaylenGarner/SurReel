from rest_framework.exceptions import APIException

class MediaLimitExceeded(APIException):
    status_code = 400
    default_detail = "You can only attach up to 10 media files to a single post. Please remove any excess files and try again."


class NoMediaForPost(APIException):
    status_code = 400
    default_detail = "You must attach at least one media file to your post. Please upload a photo or video and try again."
