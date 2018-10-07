from django.contrib import admin
from website import models

# Register your models here.
admin.site.register(models.Technology)
admin.site.register(models.Project)
admin.site.register(models.Bio)
admin.site.register(models.BlogPost)