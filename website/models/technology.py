from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name