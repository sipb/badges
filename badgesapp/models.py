from django.db import models

class BadgeType(models.Model):
    name = models.CharField(max_length=30)

class Badge(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    badge_type = models.ForeignKey(BadgeType)
    rank = models.IntegerField()
    description = models.TextField()
    picture = models.CharField(max_length=50)
    instructions = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    creator = models.CharField(20)
    secret = models.BooleanField()

class Person(models.Model):
    kerberos = models.CharField(20)
    name = models.CharField(max_length=50)
    class_year = models.IntegerField()

class Achievement(models.Model):
    person = models.ForeignKey(Person)
    badge = models.ForeignKey(Badge)
    date_acquired = models.DateField(auto_now_add=True)
    circumstances = models.TextField()
    awarder = models.ForeignKey(Person)
    status = models.CharField(max_length=50)
