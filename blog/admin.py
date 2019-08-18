from django.contrib import admin
from . import models
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug', 'post_category', 'is_active', 'pub_date', 'views')
    list_editable = ('is_active', 'post_category')
    list_filter = ('pub_date', 'is_active', 'post_category')

    class Meta:
        model = models.Posts

admin.site.register(models.Posts, PostsAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'post', 'pub_date')
    list_filter = ('author_email', 'post', 'pub_date')

    class Meta:
        model = models.Comments

admin.site.register(models.Comments, CommentsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'slug', 'is_active', 'created_date', 'views')
    list_filter = ('is_active',)
    list_editable = ('is_active',)

    class Meta:
        model = models.Category

admin.site.register(models.Category, CategoryAdmin)