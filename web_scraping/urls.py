from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_data_scraping/', views.save_data_scraping, name='save_data_scraping'),
    path('scraping/result/', views.scraping_result, name='scraping_result'),
]