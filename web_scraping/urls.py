from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scraping/', views.scraping, name='scraping'),
    path('scraping/result/', views.scraping_result, name='scraping_result'),
]