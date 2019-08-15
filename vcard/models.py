from django.db import models
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from django.urls import reverse

from django.db.models.signals import pre_save
from django.utils.html import strip_tags

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Название проекта', help_text='Введите название проекта галерии')
    project_description = RichTextUploadingField(verbose_name='Описание проекта')
    slug = AutoSlugField(populate_from='title', verbose_name='url-проекта')
    preview = models.ImageField(upload_to='uploads/gallery/', default='default_project.jpg', verbose_name='Изображение на превью')
    comp_view = models.ImageField(upload_to='uploads/gallery/comp_view/', default='comp_view.jpg', verbose_name='Изображение-результат')
    technologies = models.CharField(max_length=220, verbose_name='Использованные технологии', blank=True, null=True)
    project_url = models.URLField(max_length=200, verbose_name='Ссылка на проект', blank=True, null=True)
    seo_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Seo заголовок проекта')
    seo_description = models.TextField(max_length=220, blank=True, null=True, verbose_name='Seo описание проекта')
    seo_keywords = models.CharField(max_length=220, blank=True, null=True, verbose_name='Seo ключевые слова проекта')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'project_url': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        ordering = ['-created_date']

def gallery_seo_title_description_generator(sender, instance, *args, **kwargs):
    if instance.title and not instance.seo_title:
        instance.seo_title = instance.title

    if instance.project_description and not instance.seo_description:
        instance.seo_description = strip_tags(instance.project_description)[:170]

pre_save.connect(gallery_seo_title_description_generator, sender=Gallery)


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    favicon = models.FileField(upload_to='favicon/', blank=False, default='favicon.ico', verbose_name='Favicon для сайта')
    avatar = models.ImageField(upload_to='avatar/', blank=True, verbose_name='Аватар сайта (личное изображение)')
    my_cv = models.FileField(upload_to='files/cv/', verbose_name='Файл резюме')
    email = models.EmailField(verbose_name='Мой e-mail')
    about = RichTextUploadingField(default=None, blank=True, null=True, verbose_name='Блок обо мне на главной')
    seo_title = models.CharField(max_length=220, verbose_name='SEO заголовок главной страницы')
    seo_description = models.CharField(max_length=220, verbose_name='SEO описание главной страницы')
    seo_keywords = models.CharField(max_length=220, verbose_name='SEO ключевые слова')

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки сайта"