from django.contrib import admin
from parler.admin import TranslatableStackedInline
import nested_admin
from .models import Settings, FAQ, Page, Seo


# Register your models here.

class SeoStackedInline(TranslatableStackedInline):
    model = Seo
    extra = 1
    max_num = 1
    fieldsets = (
        (None, {"fields": (
        "page", "seo_title", "seo_description", "seo_keywords", "seo_canonical", "seo_is_robots_index",
        "seo_is_robots_follow", "json_ld_data")}),
    )


class PageAdmin(admin.ModelAdmin):
    inlines = [SeoStackedInline]
    list_display = ["id", "type", "create_at", "update_at"]
    list_filter = ["type", "create_at", "update_at"]


admin.site.register(Settings)
admin.site.register(FAQ)
admin.site.register(Page, PageAdmin)
