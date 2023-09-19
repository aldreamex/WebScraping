from django.shortcuts import render
from .models import AvitoItem
from .scraping import AvitoScrap

def home(request):
    """Парсим данные с авито"""
    scraper = AvitoScrap(url='https://www.avito.ru/bryansk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104',
               count=1,
               items=['Без комиссии, без залога', 'комнаты']
               ).scraping()

    scraper_item = AvitoItem.objects.all()
    context = {
        'scraper_item': scraper_item
    }


    return render(request, 'home.html', context)
