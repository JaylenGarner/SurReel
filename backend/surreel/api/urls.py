
from django.urls import path
from .views.posts import PostList, PostDetails, UserPosts
from .views.likes import LikeList, LikeDetails


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:post_id>/',  PostDetails.as_view()),
    path('posts/<int:post_id>/likes/', LikeList.as_view()),
    path('<int:user_id>/posts/', UserPosts.as_view()),
    path('likes/<int:like_id>/', LikeDetails.as_view())
]
