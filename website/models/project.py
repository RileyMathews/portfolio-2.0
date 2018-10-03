from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name