from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    comment = models.CharField(max_length=30)

    def __str__(self):
        return self.comment