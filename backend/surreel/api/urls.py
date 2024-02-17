
from django.urls import path
from .views.posts import PostList, PostDetails, user_posts


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:id>/',  PostDetails.as_view()),
    # path('<int:pk>/posts/', user_posts)
]
