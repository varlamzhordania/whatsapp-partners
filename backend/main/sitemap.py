from django.contrib import sitemaps
from django.urls import reverse


class HomeViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["main:home", ]

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "monthly"

    # "main:privacy", "main:terms", "main:refund"

    def items(self):
        return ["main:about", "main:contact"]

    def location(self, item):
        return reverse(item)
