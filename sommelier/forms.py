from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms

from sommelier import models


class WineForm(forms.ModelForm):
    class Meta:
        model = models.Wine
        fields = '__all__'
        labels = {
            'taste': 'Smak',
            'kind': 'Kolor',
            'country': 'Kraj produkcji',
            'type': 'Szczep',
            'name': 'Nazwa',
            'producer': 'Producent',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            layout.Div(
                layout.Div('taste', css_class='w-[49%]'),
                layout.Div('kind', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            'country',
            'type',
            'name',
            'producer',
            layout.Div(
                layout.Submit(
                    'submit',
                    'Zapisz',
                    css_class='rounded-md bg-amber-200 px-4 py-2 text-sm font-semibold shadow-sm hover:bg-amber-300 '
                              'focus-visible:outline focus-visible:outline-2',
                ),
                css_class='flex justify-center mt-4',
            ),
        )


class BottleForm(forms.ModelForm):
    class Meta:
        model = models.Bottle
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
            'year': forms.NumberInput(attrs={'value': 2020}),
            'score': forms.NumberInput(attrs={'value': 7}),
        }
        labels = {
            'wine': 'Wino',
            'year': 'Rok produkcji',
            'score': 'Ocena',
            'description': 'Opis',
            'image': 'Zdjęcie',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            'wine',
            layout.Div(
                layout.Div('year', css_class='w-[49%]'),
                layout.Div('score', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            'description',
            'image',
            layout.Div(
                layout.Submit(
                    'submit',
                    'Zapisz',
                    css_class='rounded-md bg-amber-200 px-4 py-2 text-sm font-semibold shadow-sm hover:bg-amber-300'
                              'focus-visible:outline focus-visible:outline-2',
                ),
                css_class='flex justify-center mt-4',
            ),
        )


class ShopInfoForm(forms.ModelForm):
    class Meta:
        model = models.ShopInfo
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # TODO: change display format
            'price': forms.NumberInput(attrs={'value': 20}),
        }
        labels = {
            'bottle': 'Butelka',
            'shop_name': 'Sklep',
            'price': 'Cena',
            'date': 'Data zakupu',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            'bottle',
            'shop_name',
            layout.Div(
                layout.Div('date', css_class='w-[49%]'),
                layout.Div('price', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            layout.Div(
                layout.Submit(
                    'submit',
                    'Zapisz',
                    css_class='rounded-md bg-amber-200 px-4 py-2 text-sm font-semibold shadow-sm hover:bg-amber-300'
                              'focus-visible:outline focus-visible:outline-2',
                ),
                css_class='flex justify-center mt-1.5',
            ),
        )
