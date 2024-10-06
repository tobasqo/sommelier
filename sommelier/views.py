from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from sommelier import forms, models


class BottleListView(ListView):
    model = models.Bottle
    template_name = "partials/bottle_list.html"
    context_object_name = "bottles"
    paginate_by = 2


class WineCreateView(CreateView):
    model = models.Wine
    form_class = forms.WineForm
    template_name = 'partials/forms/wine_form.html'
    success_url = reverse_lazy('bottle-create')


class BottleCreateView(CreateView):
    model = models.Bottle
    form_class = forms.BottleForm
    template_name = 'partials/forms/bottle_form.html'
    success_url = reverse_lazy('shop-info-create')


class ShopInfoCreateView(CreateView):
    model = models.ShopInfo
    form_class = forms.ShopInfoForm
    template_name = 'partials/forms/shop_info_form.html'
    success_url = reverse_lazy('bottle-list')


class BottleDetailView(DetailView):
    model = models.Bottle
    form_class = forms.BottleForm
    template_name = 'partials/bottle_detail.html'


# class WineUpdateView(UpdateView):
#     model = models.Wine
#     form_class = forms.WineForm
#     template_name = 'partials/forms/wine_form.html'
#     success_url = reverse_lazy('bottle-detail')
#
#
# class BottleUpdateView(UpdateView):
#     model = models.Bottle
#     form_class = forms.BottleForm
#     template_name = 'partials/forms/bottle_form.html'
#     success_url = reverse_lazy('bottle-detail')
#
#
# class ShopInfoUpdateView(UpdateView):
#     model = models.ShopInfo
#     form_class = forms.ShopInfoForm
#     template_name = 'partials/forms/shop_info_form.html'
#     success_url = reverse_lazy('bottle-detail')
