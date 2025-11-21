from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

class Data(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    task = models.CharField(max_length=200)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(auto_now_add=True)


