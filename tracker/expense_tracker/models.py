from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Meta:
    db_table = "user"
   

# make migrations
# 1. py manage.py makemigrations
# 2 .py manage.py migrate