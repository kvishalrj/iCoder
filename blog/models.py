from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, default="")
    title = models.CharField(max_length=255)
    postImage = models.CharField(max_length=1000, default="/static/img/blog.png")
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(default= now)

    def __str__(self) -> str:
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key= True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null = True)
    timestamp = models.DateTimeField(default= now)

    def __str__(self) -> str:
        return self.comment[0:15] + "... by " + self.user.username