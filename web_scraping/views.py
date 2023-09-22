from django.shortcuts import render
from .models import AvitoItem, FormData
from .scraping import AvitoScrap
from .forms import AvitoScrapForm
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    home_item = {
        'qwqw': 'erere'
    }
    context = {
        'home_item': home_item
    }
    return render(request, 'home.html', context)


def save_data_scraping(request):
    if request.method == 'POST':
        form = AvitoScrapForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            selected_categories = form.cleaned_data.get('categories')

            form_item = FormData(form_url=url, categories=selected_categories)
            form_item.save()

            messages.success(request, 'Данные успешно сохранены!')

    else:
        form = AvitoScrapForm()

    context = {
        'form': form
    }

    return render(request, 'save_data_scraping.html', context)


def scraping_result(request):
    form_data = FormData.objects.first()
    url = form_data.form_url
    categories = form_data.categories

    scraper = AvitoScrap(url=str(url), items=categories, count=1)
    scraper.scraping()

    scraper_item = AvitoItem.objects.all()

    print(url)
    print(categories)

    context = {
        'scraper_item': scraper_item
    }

    return render(request, 'scraping_result.html', context)
