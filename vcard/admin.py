from django.contrib import admin
from . import models
# Register your models here.

from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'project_url', 'pub_date', 'is_active')
    list_editable = ('project_url', 'is_active')
    list_filter = ('is_active', 'pub_date')

    class Meta:
        model = models.Gallery

admin.site.register(models.Gallery, GalleryAdmin)