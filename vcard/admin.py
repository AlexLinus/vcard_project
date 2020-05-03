from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from .models import SiteConfig, Gallery, Skills


admin.site.unregister(Group)


admin.site.site_header = 'VCARD'
admin.site.site_title = 'VCARD'
admin.site.index_title = 'Страница Администрации'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """ Admin for Gallery objects (Portfolio) """

    list_display = ('title', 'slug', 'project_url', 'pub_date', 'is_active')
    list_editable = ('project_url', 'is_active')
    list_filter = ('is_active', 'pub_date')

    fieldsets = (
        (None, {'fields': ('title', 'project_description', 'preview', 'comp_view', 'technologies', 'project_url',
                           'is_active')}),
        ('SEO', {'fields': ('seo_title', 'seo_description', 'seo_keywords',)}),
    )

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    """ Admin for Gallery objects (Portfolio) """

    list_display = ('title', 'percent', 'is_active')
    list_editable = ('is_active', )
    list_filter = ('is_active', 'percent')


@admin.register(SiteConfig)
class SiteConfigurationAdmin(admin.ModelAdmin):
    """ Admin for SiteConfiguration  (Singleton)"""
    fieldsets = (
        ('Настройки', {'fields': ('site_name', 'favicon')}),
        ('Обо мне', {'fields': ('name', 'nickname', 'specialization', 'avatar', 'about', 'city')}),
        ('Контакты', {'fields': ('my_cv', 'email', 'linkedin', 'skype')}),
    )

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True