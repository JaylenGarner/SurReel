from rest_framework.response import Response

from ..models import Media
from ..serializers import MediaSerializer
from ..exceptions.media import MediaLimitExceeded

# View Functions #

# Helper Functions #

def create_media(data, post_id):
    max_media_limit = 10
    media_counter = 0

    for media_data in data:

        if media_counter >= max_media_limit:
            raise MediaLimitExceeded()

        media_counter += 1
        media_data['post'] = post_id
        media_serializer = MediaSerializer(data=media_data)

        if media_serializer.is_valid():
            media_serializer.save()

    return
