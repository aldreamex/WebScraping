from django.db import models
from django.utils import timezone

class AvitoItem(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField()
    url = models.URLField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.TextField(max_length=50, default=timezone.now)

    def __str__(self):
        return self.name

class FormData(models.Model):
    form_url = models.TextField(max_length=100)
    categories = models.TextField(max_length=100, default='some_default_value')

    def __str__(self):
        return f'{self.form_url}, {self.categories}'