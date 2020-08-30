from django.db import models


# Create your models here.


class GlobalSeo(models.Model):
    """ Model for setting global SEO site settings"""

    class Meta:
        verbose_name = 'SEO настройки сайта'
        verbose_name_plural = 'SEO настройки сайта'

    # MAIN SEO BLOCK
    main_seo_title = models.CharField(
        max_length=220, verbose_name='SEO заголовок главной страницы')
    main_seo_description = models.CharField(
        max_length=220, verbose_name='SEO описание главной страницы')
    main_seo_keywords = models.CharField(
        max_length=220, verbose_name='SEO ключевые слова главной страницы')

    # BLOG SEO BLOCK
    blog_seo_title = models.CharField(
        max_length=220, verbose_name='SEO заголовок для блога')
    blog_seo_description = models.CharField(
        max_length=220, verbose_name='SEO описание для блога')
    blog_seo_keywords = models.CharField(
        max_length=220, verbose_name='SEO ключевые слова для блога')

    # PORTFOLIO SEO BLOCK
    portfolio_seo_title = models.CharField(
        max_length=220, verbose_name='SEO заголовок для блога')
    portfolio_description = models.CharField(
        max_length=220, verbose_name='SEO описание для блога')
    portfolio_seo_keywords = models.CharField(
        max_length=220, verbose_name='SEO ключевые слова для блога')

    def __str__(self):
        return 'SEO настройки сайта'


class RobotsUrlPattern(models.Model):
    """ Class for url patterns for RobotsTxt """

    class Meta:
        verbose_name = 'Robots.txt - URL-паттерн'
        verbose_name_plural = 'Robots.txt - URL-паттерн'

    url_pattern = models.CharField(
        max_length=300, verbose_name='Шаблон url',
        help_text="Внимание: учитывается регистр!"
                  "Если в конце пропущен слэш, то под шаблон попадут все файлы,"
                  " путь к которым начинается с таких же символов."
                  " Например: под шаблон «/admin' так же попадет «/admin.html»."
                  "Часть поисковых систем понимают звездочку (*) как"
                  " произвольное количество любых символов и знак доллара ($)"
                  " как символ конца URL. Например: «/*.jpg$»")

    def __str__(self):
        return self.url_pattern


class RobotsTxt(models.Model):
    """ Class for creating Robots.txt """

    class Meta:
        verbose_name = 'Robots.txt - Правила индексации'
        verbose_name_plural = 'Robots.txt - Правила индексации'

    robot = models.CharField(
        max_length=200, verbose_name='Название робота',
        help_text='Название робота (User agent). Введите звездочку (*)'
                  ' для применения правил ко всем роботов. Полный список'
                  ' можно посмотреть в базе данных веб-ботов.')
    allowed_urls = models.ManyToManyField(
        RobotsUrlPattern, blank=True, verbose_name='Разрешенные url',
        help_text='URL адреса разрешенные для индексации поисковыми роботами.',
        related_name='allowed_urls')

    disallowed_urls = models.ManyToManyField(
        RobotsUrlPattern, blank=True, verbose_name='Запрещенные url',
        related_name='disallowed_urls')

    is_active = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'Правило индексации #{self.id}'


class RobotsHost(models.Model):
    """
        Robots.txt hosts main mirror (for example alexlinus.ru/sitemap.xml)
    """

    class Meta:
        verbose_name = 'Robots.txt - Главное зеркало'
        verbose_name_plural = 'Robots.txt - Главное зеркало'

    url = models.CharField(max_length=200, verbose_name='Главное зеркало',
                           help_text='Будет указано в robots.txt как главное'
                                     ' зеркало сайта в директиве Host.'
                                     ' Например - (HOST: alexlinus.ru)')

    def __str__(self):
        return self.url
