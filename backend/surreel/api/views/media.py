from rest_framework.response import Response
from django.http import JsonResponse
from ..models import Media
from ..serializers import MediaSerializer
from ..exceptions.media import MediaLimitExceeded
from rest_framework.serializers import ValidationError
from ..utils.helper_functions import format_validation_errors


# Helper Functions #


def create_media(data, post_id):

   try:
        max_media_limit = 10
        media_counter = 0
        error = None

        for media_data in data:

            if media_counter >= max_media_limit:
                raise MediaLimitExceeded()

            media_counter += 1
            media_data['post'] = post_id
            media_serializer = MediaSerializer(data=media_data)

            if media_serializer.is_valid():
                media_serializer.save()

            else:
                raise ValidationError(media_serializer.errors)

   except MediaLimitExceeded as e:
        error = JsonResponse({"error": str(e), "status": e.status_code})
        return error

   except ValidationError as e:
        formatted_error = format_validation_errors(e)
        error = JsonResponse({"error": str(formatted_error), "status": e.status_code})
        return error
