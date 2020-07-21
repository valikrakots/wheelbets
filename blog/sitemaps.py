from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['blog-about', 'blog-help', 'blog-where', 'blog-home', 'blog-contacts']

    def location(self, item):
        return reverse(item)
