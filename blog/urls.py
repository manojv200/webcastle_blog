from django.urls import path
from . import views
from .views import PostListCreate

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('posts/',views.PostListCreate.as_view(), name="posts"),
    path('posts/<int:pk>/', views.DetailPost.as_view(), name="post-detail"),
    path('posts/<int:pk>/comments/', views.CommentCreate.as_view(), name="add-comment"),
]