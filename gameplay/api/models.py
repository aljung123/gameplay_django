from django.db import models

# Create your models here.

class user_comment(models.Model):
    comment = models.CharField(max_length=30)

    def __str__(self):
        return self.comment