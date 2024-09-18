from django import forms
from django.forms import DateInput

from sommelier import models


class WineForm(forms.ModelForm):
    class Meta:
        model = models.Wine
        fields = '__all__'


class BottleForm(forms.ModelForm):
    class Meta:
        model = models.Bottle
        fields = '__all__'


class ShopInfoForm(forms.ModelForm):
    class Meta:
        model = models.ShopInfo
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
