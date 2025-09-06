from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email= models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

