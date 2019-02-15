from django.db import models

# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_nominated = models.BooleanField(null=True)


class Poll_admin(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_time_set = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



