from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.serializers import ValidationError
from ..utils.helper_functions import format_validation_errors
from ..models import Post
from ..serializers import PostSerializer
from .media import create_media
from ..exceptions.media import NoMediaForPost



# View Functions #


'''  /  '''

@api_view(['GET', 'POST'])
@csrf_exempt
def post_list(request):

    if request.method == 'GET':
        return get_all_posts()

    elif request.method == 'POST':
        return create_post(request)


'''  /<id>  '''

@api_view(['GET', 'PATCH', 'DELETE'])
@csrf_exempt
def post_details(request, pk):

    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found", "status": 404})

    if request.method == 'GET':
       return get_post_by_id(post)

    elif request.method == 'PATCH':
        return edit_post(request, post)

    elif request.method == 'DELETE':
        return delete_post(post)


# Helper Functions #

def get_all_posts():
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    data_dict = {'posts': serializer.data}

    return JsonResponse(data_dict)


def get_post_by_id(post):
    post_serializer = PostSerializer(post)
    return JsonResponse(post_serializer.data)


def create_post(request):
    try:
        post_data = JSONParser().parse(request)
        media_data = post_data.pop('media', None)

        if media_data == None:
            raise NoMediaForPost()

        post_serializer = PostSerializer(data=post_data)

        if post_serializer.is_valid():
            post_instance = post_serializer.save()
            post_id = post_instance.id
        else:
            raise ValidationError(post_serializer.errors)

        media_error = create_media(media_data, post_id)

        if media_error is not None:
            post_instance.delete()
            return media_error

        return  JsonResponse(post_serializer.data, status=201)

    except NoMediaForPost as e:
        return JsonResponse({"error": str(e), "status" : e.status_code})

    except ValidationError as e:
        formatted_error = format_validation_errors(e)
        return JsonResponse({"errors": formatted_error, "status": 400})


def delete_post(post):
    post.delete()
    return JsonResponse({"message": "The post has been deleted", "status": 200})


def edit_post(request, post):
    try:
        data = JSONParser().parse(request)
        post_serializer = PostSerializer(post, data=data, partial=True)

        if post_serializer.is_valid():
            post_serializer.save()
            return  JsonResponse(post_serializer.data, status=200)

        else:
            raise ValidationError(post_serializer.errors)

    except ValidationError as e:
        formatted_error = format_validation_errors(e)
        return JsonResponse({"errors": formatted_error, "status": 400})
