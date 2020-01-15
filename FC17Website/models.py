from django.db import models

class Teams(models.Model):
    name = models.CharField(max_length=20)