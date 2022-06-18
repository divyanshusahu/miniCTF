from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Threads)
admin.site.register(models.Answers)