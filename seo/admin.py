from django.contrib import admin

# Register your models here.
from seo.models import (
    GlobalSeo, RobotsHost, RobotsUrlPattern, RobotsTxt
)


@admin.register(GlobalSeo)
class GlobalSeoAdmin(admin.ModelAdmin):
    """ Admin for global SEO settings """

    fieldsets = (
        ('Главная страница', {'fields': ('main_seo_title', 'main_seo_description', 'main_seo_keywords')}),
        ('Блог', {'fields': ('blog_seo_title', 'blog_seo_description', 'blog_seo_keywords')}),
        ('Портфолио', {'fields': ('portfolio_seo_title', 'portfolio_description', 'portfolio_seo_keywords')}),
        ('Контакты', {'fields': ('contact_seo_title', 'contact_seo_description', 'contact_seo_keywords')}),
    )

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True


@admin.register(RobotsTxt)
class RobotsTxtAdmin(admin.ModelAdmin):
    list_display = ('robot', 'is_active')
    list_editable = ('is_active',)

    fieldsets = (
        (None, {"fields": ("robot", 'is_active')}),
        ("URL паттерны", {"fields": ("allowed_urls", "disallowed_urls")})
    )


@admin.register(RobotsUrlPattern)
class RobotsUrlPatternAdmin(admin.ModelAdmin):
    list_display = ('url_pattern',)


@admin.register(RobotsHost)
class RobotsHostAdmin(admin.ModelAdmin):
    list_display = ('url',)

    def has_add_permission(self, request):
        return self.model.objects.count() < 1