from django.db import models


class Answer(models.Model):
    num = models.IntegerField()
    value = models.IntegerField()
