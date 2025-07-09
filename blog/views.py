from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from blog.models import Posts, Comments, TblUser
from blog.serializers import PostsSerializer, PostDetailSerializer, CommentsSerializer, RegistrationSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class PostListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all().order_by('-created_at')
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DetailPost(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        return PostsSerializer

    def perform_destroy(self, instance):
        if self.request.user!= instance.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        instance.delete()

class CommentCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        serializer.save(commenter=self.request.user, post=Posts.objects.get(pk=post_id))


