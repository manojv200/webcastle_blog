from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from blog.models import Comments, Posts, TblUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblUser
        fields = ('username', 'email', 'mobile', 'password')

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        mobile = validated_data['mobile']
        password = validated_data['password']
        user = TblUser.objects.create_user(username=username, email=email, mobile=mobile, password=password)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user_id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'mobile': instance.mobile,
            'access' : str(refresh.access_token),
            'refresh' : str(refresh),
        }

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