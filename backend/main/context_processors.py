from .models import Settings
from django.conf import settings


def Default(request):
    return {
        'page_setting': Settings.objects.first(),
        'asset_version': settings.STATIC_VERSION
    }
