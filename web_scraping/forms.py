from django import forms

class AvitoScrapForm(forms.Form):
    url = forms.URLField(label='Ссылка на Avito', required=True)
    categories = forms.MultipleChoiceField(
        label='Выберите категории',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('category1', 'Без комиссии'),
            ('category2', 'Без комиссии, без залога'),

        ]
    )