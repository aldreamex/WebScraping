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
    form_data = FormData.objects.last()
    print(form_data)
    url = form_data.form_url
    categories = form_data.categories
    categories_list = [categories.strip("[]'") if categories else "Без категории"]
    print(url)
    print(categories_list)
    # scraper = AvitoScrap(url=str(url), items=categories, count=1)
    # scraper.scraping()
    AvitoScrap(url=url, count=1, items=categories_list).scraping()
    scraper_item = AvitoItem.objects.all()
    # ЕСЛИ ПЕРЕДАЮ НАПРЯМУЮ ВСЕ ПАРСИТСЯ ЧЕТКО:
    # AvitoScrap(
    #     url='https://www.avito.ru/bryansk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA',
    #     count=1,items=['Без комиссии, без залога']).scraping()



    context = {
        'scraper_item': scraper_item
    }

    return render(request, 'scraping_result.html', context)
