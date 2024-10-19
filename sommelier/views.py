from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from sommelier import forms, models


class BottleListView(ListView):
    model = models.Bottle
    template_name = "routes/bottle_list.html"
    context_object_name = "bottles"
    paginate_by = 25


class WineCreateView(CreateView):
    model = models.Wine
    form_class = forms.WineForm
    template_name = 'routes/wine_form.html'

    def get_success_url(self):
        return reverse_lazy('bottle-create', kwargs={'wine_pk': self.object.pk})


class BottleCreateView(CreateView):
    model = models.Bottle
    form_class = forms.BottleForm
    template_name = 'routes/bottle_form.html'

    def get_success_url(self):
        return reverse_lazy('shop-info-create', kwargs={'bottle_pk': self.object.pk})

    def get_initial(self):
        return {'wine': self.kwargs['wine_pk']}


# TODO: based on previous url (bottle-detail/bottle-create) change success url
class ShopInfoCreateView(CreateView):
    model = models.ShopInfo
    form_class = forms.ShopInfoForm
    template_name = 'routes/shop_info_form.html'
    success_url = reverse_lazy('bottle-list')

    def get_initial(self):
        return {'bottle': self.kwargs['bottle_pk']}


class BottleDetailView(DetailView):
    model = models.Bottle
    form_class = forms.BottleForm
    template_name = 'routes/bottle_detail.html'


class WineUpdateView(UpdateView):
    model = models.Wine
    form_class = forms.WineForm
    template_name = 'routes/wine_form.html'

    def get_success_url(self):
        return reverse_lazy('bottle-detail', kwargs={'pk': self.kwargs['bottle_pk']})


class BottleUpdateView(UpdateView):
    model = models.Bottle
    form_class = forms.BottleForm
    template_name = 'routes/bottle_form.html'

    def get_success_url(self):
        return reverse_lazy('bottle-detail', kwargs={'pk': self.object.pk})


class ShopInfoUpdateView(UpdateView):
    model = models.ShopInfo
    form_class = forms.ShopInfoForm
    template_name = 'routes/shop_info_form.html'

    def get_success_url(self):
        return reverse_lazy('bottle-detail', kwargs={'pk': self.object.bottle.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['date'] = self.object.date  # TODO: fix
        return initial
