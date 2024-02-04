
from django.urls import path
from .views.posts import post_list, post_details, user_posts


urlpatterns = [
    path('posts/', post_list),
    path('posts/<int:pk>/', post_details),
    path('<int:pk>/posts/', user_posts)
]
