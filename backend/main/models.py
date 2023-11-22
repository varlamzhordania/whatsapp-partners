from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
PAGE_TYPE_CHOICES = (
    ("home", "Home Page"),
    ("about", "About Page"),
    ("contact", "Contact Page"),
)


def logo_image(instance, filename):
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    extension = filename.split('.')[-1]
    return f'images/website/{timestamp}.{extension}'


class Page(models.Model):
    type = models.CharField(
        max_length=255,
        choices=PAGE_TYPE_CHOICES,
        blank=False,
        null=False,
        unique=True,
        help_text=_(
            "format: create only 1 record with types, example only create 1 home page record rest won't be count except category"
        )
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Create"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Modified"))

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.type


class Seo(TranslatableModel):
    page = models.OneToOneField(
        Page, related_name="page_seo", blank=False, null=False,
        verbose_name=_("Belonging Page"), on_delete=models.CASCADE
    )
    translations = TranslatedFields(
        seo_title=models.CharField(
            max_length=255, blank=False, null=False, verbose_name=_("Seo Title"),
            help_text=_("For SEO purposes, ideally between 60-70 characters.")
        ),
        seo_description=models.TextField(
            max_length=160, blank=False, null=False, verbose_name=_("Seo Description"),
            help_text=_("For SEO purposes, ideally between 150-160 characters.")
        ),
        seo_keywords=models.TextField(
            blank=False, null=False, verbose_name=_("Seo Keywords"),
            help_text=_("Comma-separated list of keywords.")
        ),
    )
    seo_canonical = models.URLField(blank=False, null=False, verbose_name=_("Seo Canonical"))
    seo_is_robots_index = models.BooleanField(
        default=False, verbose_name=_("Seo Robot Index"),
        help_text=_("Set to allow search engines to index this page.")
    )
    seo_is_robots_follow = models.BooleanField(
        default=False, verbose_name=_("Seo Robot Follow"),
        help_text=_("Set to allow search engines to follow links on this page.")
    )
    json_ld_data = models.TextField(
        blank=True, null=True, verbose_name="JSON-LD Data",
        help_text="Enter JSON-LD data for structured information (if applicable)."
    )

    class Meta:
        verbose_name = _("SEO")
        verbose_name_plural = _("SEO")

    def __str__(self):
        return str(self.id)


class FAQ(models.Model):
    question = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_("Question"),
        help_text=_("format: max-255 , required")
    )
    answer = models.TextField(
        verbose_name=_("Answer"),
        blank=False, null=False,
        help_text=_("format: required")
    )
    is_active = models.BooleanField(verbose_name=_("Published"), default=False)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Create"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Modified"))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")
        ordering = ["-id"]

    def __str__(self):
        return self.question


class ContactUs(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"), blank=False, null=False)
    email = models.EmailField(verbose_name=_("Email"), blank=False, null=False)
    message = models.TextField(
        max_length=600,
        verbose_name=_("Message"),
        help_text=_("format:required , max-3000"),
        blank=False,
        null=False
    )
    is_check = models.BooleanField(verbose_name=_("Is Check"), default=False)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Create"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Modified"))

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.id}-{self.name}"


class Settings(models.Model):
    site_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name=_("Site Name"),
        help_text=_("format:max-255, the name of website")
    )

    primary_logo = models.ImageField(
        upload_to=logo_image,
        blank=True,
        null=True,
        verbose_name=_("Primary Logo"),
        help_text=_("format: JPEG,JPG,PNG,SVG,WEBP")
    )
    secondary_logo = models.ImageField(
        upload_to=logo_image,
        blank=True,
        null=True,
        verbose_name=_("Secondary Logo"),
        help_text=_("format: JPEG,JPG,PNG,SVG,WEBP")
    )
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Physical Address"))
    facebook = models.URLField(verbose_name=_("Facebook"), help_text=_("format: absolute URL"), blank=True, null=True)
    instagram = models.URLField(verbose_name=_("Instagram"), help_text=_("format: absolute URL"), blank=True, null=True)
    x_twitter = models.URLField(
        verbose_name=_("X(Twitter)"),
        help_text=_("format: absolute URL,"),
        blank=True,
        null=True
    )
    youtube = models.URLField(verbose_name=_("Youtube"), help_text=_("format: absolute URL"), blank=True, null=True)
    api_token = models.TextField(
        verbose_name=_("Api Token"),
        help_text=_("format: used in post request to create campaign"),
        blank=True,
        null=True, )
