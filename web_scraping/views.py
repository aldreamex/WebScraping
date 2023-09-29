from django.shortcuts import render
from .models import AvitoItem, FormData
from .scraping import AvitoScrap
from .forms import AvitoScrapForm
from django.shortcuts import render, redirect
from django.contrib import messages
import ast


def home(request):
    return render(request, 'home.html')


def save_data_scraping(request):
    if request.method == 'POST':
        form = AvitoScrapForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            selected_categories = form.cleaned_data.get('categories')

            try:
                form_item = FormData(form_url=url, categories=selected_categories)
                form_item.save()
                messages.success(request, 'Данные успешно сохранены!')

            except IntegrityError as e:
                error_message = f"Произошла ошибка при сохранении данных в БД: {str(e)}"
                messages.error(request, error_message)

    else:
        form = AvitoScrapForm()

    context = {
        'form': form
    }

    return render(request, 'save_data_scraping.html', context)


def scraping_result(request):
    try:
        form_data = FormData.objects.last()

        if not form_data or not form_data.form_url:
            messages.error(request, 'Пожалуйста, введите URL')
            return redirect('save_data_scraping')

        # print(form_data)

        url = form_data.form_url
        categories = form_data.categories

        try:
            categories_list = ast.literal_eval(categories)
        except (ValueError, SyntaxError):
            categories_list = ["Без категории"]

        # print(url)
        # print(categories_list)

        AvitoScrap(url=url, count=1, items=categories_list).scraping()
        scraper_item = AvitoItem.objects.all()

        context = {
            'scraper_item': scraper_item
        }

        return render(request, 'scraping_result.html', context)

    except  (WebDriverException, ValueError) as e:
        error_message = f"Произошла ошибка: {str(e)}"
        messages.error(request, error_message)
        return redirect('home')
