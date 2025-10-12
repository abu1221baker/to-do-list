from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Data(models.Model):
    task = models.CharField(max_length=200)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(auto_now_add=True)


