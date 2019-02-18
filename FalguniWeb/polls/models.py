from django.db import models

# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_nominated_PM = models.BooleanField(null=True)
    is_nominated_mayor = models.BooleanField(null=True)
    is_nominated_councillor = models.BooleanField(null=True)
    vote_casted = models.BooleanField(null=True)
    votes_count_PM = models.IntegerField(default=0)
    votes_count_mayor = models.IntegerField(default=0)
    votes_count_councillor = models.IntegerField(default=0)


class Poll_admin(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_time_set = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class PM(models.Model):
    email = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)


class Mayor(models.Model):
    email = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)

class Councillor(models.Model):
    email = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)