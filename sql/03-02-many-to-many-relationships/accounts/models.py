from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    #symmetrical=False -> 영희가 철수를 팔로우해도 철수가 영희를 팔로우되지 않음