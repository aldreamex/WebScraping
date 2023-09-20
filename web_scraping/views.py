from django.shortcuts import render
from .models import AvitoItem
from .scraping import AvitoScrap
from .forms import AvitoScrapForm
from django.shortcuts import render, redirect


def home(request):
    home_item = {
        'qwqw': 'erere'
    }
    context = {
        'home_item': home_item
    }

    return render(request, 'home.html', context)

def scraping(request):
    if request.method == 'POST':
        form = AvitoScrapForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            selected_categories = form.cleaned_data.get('categories')
            scraper = AvitoScrap(url=url, items=selected_categories, count=1)

            # Сохраняем значения в сессии
            request.session['url'] = url
            request.session['selected_categories'] = selected_categories

            return redirect('scraping_result')

    else:
        form = AvitoScrapForm()

    context = {
        'form': form
    }

    return render(request, 'scraping.html', context)


def scraping_result(request):
    """Парсим данные с авито"""
    # Извлекаем значения из сессии
    url = 'https://www.avito.ru/bryansk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?s=104'
    # selected_categories = request.session.get('selected_categories', [])
    # selected_categories = [choice[0] for choice in selected_categories]
    selected_categories = ['Без комиссии']
    print(url)
    print(selected_categories)
    scraper = AvitoScrap(url=str(url), items=selected_categories, count=1).scraping()

    scraper_item = AvitoItem.objects.all()
    context = {
        'scraper_item': scraper_item
    }


    return render(request, 'scraping_result.html', context)
