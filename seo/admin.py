from django.contrib import admin

# Register your models here.
from seo.models import GlobalSeo


@admin.register(GlobalSeo)
class GlobalSeoAdmin(admin.ModelAdmin):
    """ Admin for global SEO settings """

    fieldsets = (
        ('Главная страница', {'fields': ('main_seo_title', 'main_seo_description', 'main_seo_keywords')}),
        ('Блог', {'fields': ('blog_seo_title', 'blog_seo_description', 'blog_seo_keywords')}),
        ('Портфолио', {'fields': ('portfolio_seo_title', 'portfolio_description', 'portfolio_seo_keywords')}),
    )

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True
