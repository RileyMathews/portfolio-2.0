from django.db import models

class Bio(models.Model):
    content = models.TextField()
