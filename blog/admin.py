from django.contrib import admin

from .models import Posts, Comments, Category
# Register your models here.


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug', 'post_category', 'is_active', 'pub_date', 'views')
    list_editable = ('is_active', 'post_category')
    list_filter = ('pub_date', 'is_active', 'post_category')

    fieldsets = (
        (None, {'fields': ('post_title', 'post_body', 'post_category', 'preview_image', 'is_active', 'slug')}),
        ('SEO', {'fields': ('seo_title', 'seo_description', 'seo_keywords', 'views',)}),
    )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'post', 'pub_date')
    list_filter = ('author_email', 'post', 'pub_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'slug', 'is_active', 'created_date', 'views')
    list_filter = ('is_active',)
    list_editable = ('is_active',)

    fieldsets = (
        (None, {'fields': ('category_title', 'category_description', 'is_active', )}),
        ('SEO', {'fields': ('seo_title', 'seo_description', 'seo_keywords', 'views',)}),
    )