from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ, Page
from core.utils import fancy_message
from django.core.cache import cache
from .forms import ContactUsForm
from django.utils.translation import gettext as _


def home(request, *args, **kwargs):
    page_data = cache.get("home_page")

    if page_data is not None:
        page = page_data
    else:
        page = Page.objects.filter(type="home").first()
        cache.set('home_page', page, 900)

    my_context = {
        "Title": "Home",
        "page": page
    }
    return render(request, "main/home.html", my_context)


def about(request, *args, **kwargs):
    page_data = cache.get("about_page")

    if page_data is not None:
        page = page_data
    else:
        page = Page.objects.filter(type="about").first()
        cache.set('about_page', page, 900)

    my_context = {
        "Title": "About US",
        "page": page
    }
    return render(request, "main/about.html", my_context)


def contact(request, *args, **kwargs):
    if request.method == "POST":
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            fancy_message(
                request,
                _("Our support will review and answer you as soon as possible"),
                level="success"
            )
            return redirect("main:contact")
        else:
            fancy_message(request, form.errors, level="error")

    page_data = cache.get("contact_page")

    if page_data is not None:
        page = page_data
    else:
        page = Page.objects.filter(type="contact").first()
        cache.set('contact_page', page, 900)

    form = ContactUsForm(request.POST)

    my_context = {
        "Title": "Contact US",
        "page": page,
        "form": form
    }
    return render(request, "main/contact.html", my_context)
