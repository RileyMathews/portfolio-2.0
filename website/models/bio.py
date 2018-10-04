from django.db import models

class Bio(models.Model):
    content = models.CharField(max_length=10000)
