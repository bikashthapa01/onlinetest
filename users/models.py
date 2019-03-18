from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
	is_user = models.BooleanField(default=False)
	is_mod = models.BooleanField(default=False)

	def __str__(self):
		return self.username




