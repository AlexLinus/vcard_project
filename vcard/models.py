from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.html import strip_tags
from django.core.validators import MinValueValidator, MaxValueValidator

from seo.mixins import SeoAbstractModel
# Create your models here.


class Gallery(SeoAbstractModel):
    title = models.CharField(max_length=200, blank=False, null=False,
                             verbose_name='Название проекта',
                             help_text='Введите название проекта галерии')
    project_description = RichTextUploadingField(verbose_name='Описание проекта')
    slug = AutoSlugField(populate_from='title', verbose_name='url-проекта')
    preview = models.ImageField(upload_to='uploads/gallery/',
                                default='default_project.jpg',
                                verbose_name='Изображение на превью')
    comp_view = models.ImageField(upload_to='uploads/gallery/comp_view/',
                                  default='comp_view.jpg',
                                  verbose_name='Изображение-результат')
    technologies = models.CharField(
        max_length=220, verbose_name='Использованные технологии',
        blank=True, null=True)
    project_url = models.URLField(
        max_length=200, verbose_name='Ссылка на проект', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Дата публикации')
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'project_url': self.slug})

    def __str__(self):
        return str(self.title)

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


class SiteConfig(models.Model):
    """ Model for setting Site Configurations (Singleton) """
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    # SITE CONFIGS BLOCK
    site_name = models.CharField(max_length=255, default='Site Name')
    favicon = models.FileField(upload_to='favicon/', blank=False,
                               default='favicon.ico',
                               verbose_name='Favicon для сайта')

    # ABOUT ME block
    name = models.CharField(max_length=200, blank=False, null=False,
                            verbose_name='Имя на главной')
    nickname = models.CharField(max_length=150, blank=True, null=True,
                                verbose_name='Никнейм на главной')
    specialization = models.CharField(max_length=150, blank=True, null=True,
                                      verbose_name='Позиция (специализация)')

    avatar = models.ImageField(upload_to='avatar/', blank=True,
                               verbose_name='Аватар сайта (личное изображение)')
    about = RichTextUploadingField(default=None, blank=True, null=True,
                                   verbose_name='Блок обо мне на главной')
    city = models.CharField(max_length=120, blank=True, null=True,
                            verbose_name='Текущий город')

    # FILES AND LINKS
    my_cv = models.FileField(upload_to='files/cv/', blank=True, null=True,
                             verbose_name='Файл резюме')
    email = models.EmailField(verbose_name='Мой e-mail')
    linkedin = models.URLField(blank=True, null=True,
                               verbose_name='Ссылка на LinkEdin')
    skype = models.CharField(max_length=120, blank=True, null=True,
                             verbose_name='Ссылка на Skype')

    header_scripts = models.TextField(blank=True,
                                      verbose_name='Скрипты в шапке сайта')
    footer_scripts = models.TextField(blank=True,
                                      verbose_name='Скрипты в подвале сайта')
    is_services_active = models.BooleanField(
        default=True,
        verbose_name='Включить блок Мои услуги на главной'
    )
    is_portfolio_active = models.BooleanField(
        default=True,
        verbose_name='Включить портфолио'
    )

    def __str__(self):
        return "Настройки сайта"


class Skills(models.Model):
    """ Model for setting skills to main page """
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    title = models.CharField(max_length=120, verbose_name='Заголовок навыка')
    percent = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='% знания навыка', help_text='От 0 до 100')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return str(self.title)