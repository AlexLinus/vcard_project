from django.db import models

# Create your models here.


class GlobalSeo(models.Model):
    """ Model for setting global SEO site settings"""
    class Meta:
        verbose_name = 'SEO настройки сайта'
        verbose_name_plural = 'SEO настройки сайта'

    # MAIN SEO BLOCK
    main_seo_title = models.CharField(max_length=220, verbose_name='SEO заголовок главной страницы')
    main_seo_description = models.CharField(max_length=220, verbose_name='SEO описание главной страницы')
    main_seo_keywords = models.CharField(max_length=220, verbose_name='SEO ключевые слова главной страницы')

    # BLOG SEO BLOCK
    blog_seo_title = models.CharField(max_length=220, verbose_name='SEO заголовок для блога')
    blog_seo_description = models.CharField(max_length=220, verbose_name='SEO описание для блога')
    blog_seo_keywords = models.CharField(max_length=220, verbose_name='SEO ключевые слова для блога')

    # PORTFOLIO SEO BLOCK
    portfolio_seo_title = models.CharField(max_length=220, verbose_name='SEO заголовок для блога')
    portfolio_description = models.CharField(max_length=220, verbose_name='SEO описание для блога')
    portfolio_seo_keywords = models.CharField(max_length=220, verbose_name='SEO ключевые слова для блога')

    def __str__(self):
        return 'SEO настройки сайта'