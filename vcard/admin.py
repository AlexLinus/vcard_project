from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Gallery)

from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)
