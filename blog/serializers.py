from rest_framework import serializers

from blog.models import Comments, Posts


class CommentsSerializer(serializers.ModelSerializer):
    commenter  = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comments
        fields = ['id', 'commenter', 'content', 'created_at']

class PostsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Posts
        fields = ['id', 'title', 'description', 'user', 'created_at']


class PostDetailSerializer(PostsSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta(PostsSerializer.Meta):
        fields = PostsSerializer.Meta.fields + ['comments']