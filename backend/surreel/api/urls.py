
from django.urls import path
from .views.posts import PostList, PostDetails, UserPosts
from .views.likes import LikeList


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:id>/',  PostDetails.as_view()),
    path('posts/<int:id>/likes/', LikeList.as_view()),
    path('<int:user_id>/posts/', UserPosts.as_view()),
]
