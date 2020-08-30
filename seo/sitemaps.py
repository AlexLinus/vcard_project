from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Category, Posts


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.filter(is_active=True)


class PostsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Posts.objects.filter(is_active=True)


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home_url', 'contact_url', 'portfolio_url']

    def location(self, item):
        return reverse(item)