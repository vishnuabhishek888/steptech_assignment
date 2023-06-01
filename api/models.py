from django.db import models

# Create your models here.

class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    role=models.CharField(max_length=50)
