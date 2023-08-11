from django.db import models

from tehran.dal.behaviors import Authorable, Timestampable


class Post(Timestampable, Authorable, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
