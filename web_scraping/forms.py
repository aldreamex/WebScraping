from django import forms

class AvitoScrapForm(forms.Form):
    url = forms.URLField(label='Ссылка на Avito', required=True)
    categories = forms.MultipleChoiceField(
        label='Предпочтения',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('Без комиссии', 'Без комиссии'),
            ('Без залога', 'Без залога'),
            ('Холодильник', 'Холодильник'),
            ('Стиральная машина', 'Стиральная машина'),
            ('Телевизор', 'Телевизор'),
            ('Балкон', 'Балкон'),
            ('Санузел: совмещенный', 'Санузел: совмещенный'),
            ('Санузел: раздельный', 'Санузел: раздельный'),
        ]
    )