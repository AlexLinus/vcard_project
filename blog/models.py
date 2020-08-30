import collections

from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField

# Create your models here.
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe



from seo.mixins import SeoAbstractModel


class Posts(SeoAbstractModel):
    """" Model for blog posts """
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_date']

    post_title = models.CharField(max_length=180, blank=False, null=False, verbose_name='Заголовок статьи')
    post_body = RichTextUploadingField(verbose_name='Текст статьи')
    slug = AutoSlugField(populate_from='post_title', unique_with=['id', 'pub_date__day'])
    post_category = models.ForeignKey('Category', related_name='category_posts', on_delete=models.CASCADE)
    preview_image = models.ImageField(upload_to='uploads/blog_previews/', default=None, blank=True, null=True,
                                      verbose_name='Превью статьи')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return str(self.post_title)

    @property
    def generate_keywords(self):
        """ Property for generating seo keywords """
        if not self.seo_keywords:
            text_count = collections.Counter(mark_safe(self.post_body).split())
            seo_words = []
            for word in text_count.most_common(12):
                if len(word[0]) > 5:
                    # убираем все символы, крому буквы
                    seo_words.append(''.join(l for l in word[0] if l.isalpha() or l.isdigit()))
            return ','.join(seo_words)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


def post_seo_title_description_keys_generator(sender, instance, *args, **kwargs):
    if instance.post_title and not instance.seo_title:
        instance.seo_title = instance.post_title

    if instance.post_body and not instance.seo_description:
        instance.seo_description = strip_tags(instance.post_body)[:170]

    if not instance.seo_keywords:
        instance.seo_keywords = instance.generate_keywords


pre_save.connect(post_seo_title_description_keys_generator, sender=Posts)


class Category(SeoAbstractModel):
    """ Model for blog categories """
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_date']

    category_title = models.CharField(max_length=130, blank=False, null=False, verbose_name='Заголовок категории')
    category_description = models.TextField(blank=True, null=True, verbose_name='Описание категории',
                                            help_text='Если понадобиться вывести текст в категории для SEO')
    slug = AutoSlugField(populate_from='category_title', unique_with=['id', 'created_date__day'])
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return str(self.category_title)

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})


def category_seo_title_description_generator(sender, instance, *args, **kwargs):
    if instance.category_title and not instance.seo_title:
        instance.seo_title = instance.category_title

    if instance.category_description and not instance.seo_description:
        instance.seo_description = strip_tags(instance.category_description)[:170]


pre_save.connect(category_seo_title_description_generator, sender=Category)


class Comments(models.Model):
    """ Model for Comments to blog posts"""
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']

    author_name = models.CharField(max_length=60, verbose_name='Автор комментария', blank=False, null=False)
    author_email = models.EmailField(verbose_name='E-mail автора комментария', blank=False, null=False)
    comment_body = models.TextField(verbose_name='Текст комментария', max_length=250)
    post = models.ForeignKey('Posts', blank=False, null=False, verbose_name='Статья', related_name='post_comments',
                             on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.id} Коммент оqт {self.author_name}, {self.pub_date}'
