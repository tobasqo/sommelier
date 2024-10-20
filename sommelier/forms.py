from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms

from sommelier import models

BLANK_OPTION = [('', 'Wybierz...')]


class BottlesFilterForm(forms.Form):
    # TODO: fix multiple choice select
    taste = forms.ChoiceField(label='Smak', choices=BLANK_OPTION + models.Taste.choices, required=False)
    kind = forms.ChoiceField(label='Kolor', choices=BLANK_OPTION + models.Kind.choices, required=False)
    countries = forms.MultipleChoiceField(label='Kraje', choices=models.Country.choices, required=False)
    type = forms.CharField(label='Szczep', max_length=models.Wine.TYPE_MAX_LENGTH, required=False)
    name = forms.CharField(label='Nazwa', max_length=models.Wine.NAME_MAX_LENGTH, required=False)
    producer = forms.CharField(label='Producent', max_length=models.Wine.PRODUCER_MAX_LENGTH, required=False)
    year_from = forms.IntegerField(
        label='Rok od',
        min_value=models.Bottle.YEAR_MIN,
        max_value=models.Bottle.YEAR_MAX,
        step_size=1,
        required=False
    )
    year_to = forms.IntegerField(
        label='Rok do',
        min_value=models.Bottle.YEAR_MIN,
        max_value=models.Bottle.YEAR_MAX,
        step_size=1,
        required=False
    )
    score_from = forms.FloatField(
        label='Ocena od',
        min_value=models.Bottle.SCORE_MIN,
        max_value=models.Bottle.SCORE_MAX,
        step_size=0.1,
        required=False
    )
    score_to = forms.FloatField(
        label='Ocena do',
        min_value=models.Bottle.SCORE_MIN,
        max_value=models.Bottle.SCORE_MAX,
        step_size=0.1,
        required=False
    )
    keywords = forms.CharField(label='Szukaj w opisie', max_length=255, required=False)
    shops = forms.MultipleChoiceField(label='Sklepy', choices=models.Shop.choices, required=False)
    price_from = forms.FloatField(label='Cena od', min_value=models.PurchaseInfo.PRICE_MIN, step_size=0.01, required=False)
    price_to = forms.FloatField(label='Cena do', step_size=0.01, required=False)
    date_from = forms.DateField(
        label='Data zakupu od',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )
    date_to = forms.DateField(
        label='Data zakupu do',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_id = 'filter-form'
        self.helper.layout = layout.Layout(
            layout.Div(
                layout.Div('taste', css_class='w-[49%]'),
                layout.Div('kind', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            'type',
            'name',
            'producer',
            layout.Div(
                layout.Div('year_from', css_class='w-[49%]'),
                layout.Div('year_to', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            layout.Div(
                layout.Div('score_from', css_class='w-[49%]'),
                layout.Div('score_to', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            layout.Div(
                layout.Div('countries', css_class='w-[49%]'),
                layout.Div('shops', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            layout.Div(
                layout.Div('price_from', css_class='w-[49%]'),
                layout.Div('price_to', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            layout.Div(
                layout.Div('date_from', css_class='w-[49%]'),
                layout.Div('date_to', css_class='w-[49%]'),
                css_class='flex justify-between',
            ),
            'keywords',
            layout.Div(
                layout.Button(
                    'clear-params',
                    value='Wyczyść',
                    css_id='clear-params',
                    css_class='rounded-md bg-amber-200 px-4 py-2 text-sm font-semibold shadow-sm hover:bg-amber-300 '
                              'focus-visible:outline focus-visible:outline-2',
                ),
                layout.Submit(
                    'submit',
                    'Szukaj',
                    css_class='rounded-md bg-amber-200 px-4 py-2 text-sm font-semibold shadow-sm hover:bg-amber-300 '
                              'focus-visible:outline focus-visible:outline-2',
                ),
                css_class='flex justify-center mt-4 gap-6',
            ),
        )


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


class PurchaseInfoForm(forms.ModelForm):
    class Meta:
        model = models.PurchaseInfo
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
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
        if 'initial' in kwargs and 'date' in kwargs['initial']:
            self.initial['date'] = kwargs['initial']['date'].strftime('%Y-%m-%d')
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
