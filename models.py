from django.db import models
from django.contrib.auth.models import User

class led (models.Model):
    key = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, unique = True)
    mode = models.IntegerField()
    value = models.IntegerField()
    colorr = models.IntegerField()
    colorb = models.IntegerField()
    colorg = models.IntegerField()
