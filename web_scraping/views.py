from django.shortcuts import render


def home(request):
    """Парсим данные с авито"""

    return render(request, 'home.html')
