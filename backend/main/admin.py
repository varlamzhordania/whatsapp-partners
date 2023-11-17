from django.contrib import admin
from .models import Settings, Page, Seo, FAQ
import nested_admin
from .forms import PageAdminForm


# Register your models here.
class SeoStackedInline(nested_admin.NestedStackedInline):
    model = Seo
    extra = 1
    max_num = 1


class PageStackedInline(nested_admin.NestedStackedInline, ):
    model = Page
    form = PageAdminForm
    inlines = [SeoStackedInline]
    extra = 1
    max_num = 1


class PageAdmin(nested_admin.NestedModelAdmin):
    inlines = [SeoStackedInline]
    list_display = ["id", "type", "create_at", "update_at"]
    list_filter = ["type", "create_at", "update_at"]


admin.site.register(Settings)
admin.site.register(FAQ)
admin.site.register(Page, PageAdmin)
