from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.html import strip_tags

class Posts(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_date']

    post_title = models.CharField(max_length=180, blank=False, null=False, verbose_name='Заголовок статьи')
    post_body = RichTextUploadingField(verbose_name='Текст статьи')
    slug = AutoSlugField(populate_from='post_title', unique_with=['id', 'pub_date__day'])
    post_category = models.ForeignKey('Category', related_name='category_posts', on_delete=models.CASCADE)
    seo_title = models.CharField(max_length=180, blank=True, null=True, verbose_name='SEO заголовок')
    seo_description = models.TextField(blank=True, null=True, verbose_name='SEO описание')
    seo_keywords = models.CharField(max_length=180, blank=True, null=True, verbose_name='SEO ключевые слова')
    preview_image = models.ImageField(upload_to='uploads/blog_previews/', default=None, blank=True, null=True, verbose_name='Превью статьи')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'post_slug': self.slug})


def post_seo_title_description_generator(sender, instance, *args, **kwargs):
    if instance.post_title and not instance.seo_title:
        instance.seo_title = instance.post_title

    if instance.post_body and not instance.seo_description:
        instance.seo_description = strip_tags(instance.post_body)[:170]


pre_save.connect(post_seo_title_description_generator, sender=Posts)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_date']

    category_title = models.CharField(max_length=130, blank=False, null=False, verbose_name='Заголовок категории')
    category_description = models.TextField(blank=True, null=True, verbose_name='Описание категории', help_text='Если понадобиться вывести текст в категории для SEO')
    slug = AutoSlugField(populate_from='category_title', unique_with=['id', 'created_date__day'])
    seo_title = models.CharField(max_length=180, blank=True, null=True, verbose_name='SEO заголовок')
    seo_description = models.TextField(blank=True, null=True, verbose_name='SEO описание')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'category_slug': self.slug})


def category_seo_title_description_generator(sender, instance, *args, **kwargs):
    if instance.category_title and not instance.seo_title:
        instance.seo_title = instance.category_title

    if instance.category_description and not instance.seo_description:
        instance.seo_description = strip_tags(instance.category_description)[:170]

pre_save.connect(category_seo_title_description_generator, sender=Category)

class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']

    author_name = models.CharField(max_length=60, verbose_name='Автор комментария', blank=False, null=False)
    author_email = models.EmailField(verbose_name='E-mail автора комментария', blank=False, null=False)
    comment_body = models.TextField(verbose_name='Текст комментария', max_length=250)
    parrent_comment = models.ForeignKey('self', blank=True, null=True, verbose_name='Родительский комментарий', related_name='children_comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', blank=False, null=False, verbose_name='Статья', related_name='post_comments', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.id} Коммент оqт {self.author_name}, {self.pub_date}'