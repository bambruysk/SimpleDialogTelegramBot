from django.db import models

# Create your models here.


class Question(models.Model):
    ask = models.CharField(max_length=256)
    answer = models.TextField(max_length=4000)


