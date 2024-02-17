
from django.urls import path
from .views.posts import PostList, post_details, user_posts


urlpatterns = [
    path('posts/', PostList.as_view()),
    # path('posts/<int:pk>/', post_details),
    # path('<int:pk>/posts/', user_posts)
]
