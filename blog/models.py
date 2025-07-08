from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.

class TblUser(AbstractUser, PermissionsMixin):
    token_version = models.IntegerField(default=1)
    mobile = models.CharField(null=True, blank=True, max_length=13)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'tbl_user'

class Posts(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(TblUser, on_delete=models.CASCADE,related_name='posts')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'posts'

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(TblUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)