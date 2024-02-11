from ..serializers import MediaSerializer

def create_media(data, post_id):
    media_limit = 10
    media_counter = 0

    for media_data in data:

        if media_counter > media_limit:
            return {"detail" : f"A post can have a maximum of 10 media files, you have attached {media_counter}."}

        media_counter += 1
        media_data['post'] = post_id
        media_serializer = MediaSerializer(data=media_data)

        if media_serializer.is_valid():
            media_serializer.save()

        else:
            return media_serializer.errors

    return
