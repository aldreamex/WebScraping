# Generated by Django 4.2.5 on 2023-09-26 06:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0004_formdata_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='avitoitem',
            name='created_at',
            field=models.TextField(default=django.utils.timezone.now, max_length=50),
        ),
    ]
