from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Comments)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug', 'post_category', 'is_active', 'pub_date', 'views')
    list_editable = ('is_active', 'post_category')
    list_filter = ('pub_date', 'is_active', 'post_category')

    class Meta:
        model = models.Posts

admin.site.register(models.Posts, PostsAdmin)