# Generated by Django 4.2.5 on 2023-09-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0003_remove_formdata_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='categories',
            field=models.TextField(default='some_default_value', max_length=100),
        ),
    ]
