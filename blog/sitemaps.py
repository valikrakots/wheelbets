from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['blog:blog-about', 'blog:blog-help', 'blog:blog-where', 'blog:blog-home', 'blog:blog-contacts']

    def location(self, item):
        return reverse(item)
