from django.db import models
from django.utils.timezone import now

# Create your models here.
class Writer(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000, default="")
    userImage  = models.ImageField(upload_to='blog/user', default='blog/user/default_user.png')

    def __str__(self) -> str:
        return self.firstName + self.lastName
