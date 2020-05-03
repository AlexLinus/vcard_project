from django.db import models


class SeoAbstractModel(models.Model):
    """ Mixin for SEO in models """

    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=300, verbose_name='SEO заголовок', blank=True, null=True)
    seo_description = models.TextField(verbose_name='SEO описание', blank=True, null=True)
    seo_keywords = models.CharField(max_length=300, verbose_name='SEO ключевые слова', blank=True, null=True)