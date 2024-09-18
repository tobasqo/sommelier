from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import DateInput

from sommelier import models


class WineForm(forms.ModelForm):
    class Meta:
        model = models.Wine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            layout.Div(
                layout.Div('taste', css_class='md:w-[50%]'),
                layout.Div('kind', css_class='md:w-[50%]'),
                css_class='md:flex md:justify-between',
            ),
            'country',
            'type',
            'name',
            'producer',
            layout.Div(
                layout.Submit(
                    'submit',
                    'Zapisz',
                    css_class='rounded-md bg-amber-200 px-4 py-2 text-sm font-semibold shadow-sm hover:bg-amber-500 '
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
        }


class ShopInfoForm(forms.ModelForm):
    class Meta:
        model = models.ShopInfo
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
