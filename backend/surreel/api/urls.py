
from django.urls import path
from .views.posts import PostList, PostDetails, UserPosts


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:id>/',  PostDetails.as_view()),
    path('<int:user_id>/posts/', UserPosts.as_view())
]
