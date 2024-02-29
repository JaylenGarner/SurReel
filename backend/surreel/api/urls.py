
from django.urls import path
from .views.posts import PostList, PostDetails, UserPosts
from .views.likes import LikePost, UnlikePost
from .views.follows import FollowUser


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:post_id>/',  PostDetails.as_view()),
    path('posts/<int:post_id>/like/', LikePost.as_view()),
    path('posts/<int:post_id>/unlike/', UnlikePost.as_view()),
    path('<int:user_id>/posts/', UserPosts.as_view()),
    path('<int:user_id>/follow/', FollowUser.as_view())
]
