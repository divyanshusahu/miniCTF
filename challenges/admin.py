from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Challenges)
admin.site.register(models.ChallengesSolvedBy)