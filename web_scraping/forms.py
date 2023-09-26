from django import forms

class AvitoScrapForm(forms.Form):
    url = forms.URLField(label='Ссылка на Avito', required=True)
    categories = forms.MultipleChoiceField(
        label='Выберите категории',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('Без комиссии', 'Без комиссии'),
            ('без залога', 'без залога'),

        ]
    )