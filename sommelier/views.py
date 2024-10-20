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
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = forms.BottlesFilterForm()
        return ctx

    # noinspection DuplicatedCode
    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        params = self.request.GET
        print(params)

        if taste := params.get("taste"):
            qs = qs.filter(wine__taste=taste)
        if kind := params.get("kind"):
            qs = qs.filter(wine__kind=kind)
        if countries := params.get("countries"):
            qs = qs.filter(wine__country__in=countries.split(','))
        if wine_type := params.get("type"):
            print(type(wine_type), wine_type)
            qs = qs.filter(wine__type__icontains=wine_type)
        if name := params.get("name"):
            qs = qs.filter(wine__name__icontains=name)
        if producer := params.get("producer"):
            qs = qs.filter(wine__producer__icontains=producer)
        if year_from := params.get("year_from"):
            qs = qs.filter(year__gte=year_from)
        if year_to := params.get("year_to"):
            qs = qs.filter(year__lte=year_to)
        if score_from := params.get("score_from"):
            qs = qs.filter(score__gte=score_from)
        if score_to := params.get("score_to"):
            qs = qs.filter(score__lte=score_to)
        if keywords := params.get('keywords'):
            qs = qs.filter(description__icontains=keywords)
        if shops := params.get("shops"):
            qs = qs.filter(purchases__shop_name__in=shops.split(','))
        if price_from := params.get("price_from"):
            qs = qs.filter(purchases__price__gte=price_from)
        if price_to := params.get("price_to"):
            qs = qs.filter(purchases__price__lte=price_to)
        if date_from := params.get("date_from"):
            qs = qs.filter(purchases__date__gte=date_from)
        if date_to := params.get("date_to"):
            qs = qs.filter(purchases__date__lte=date_to)
        print(qs)
        return qs


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
        return reverse_lazy('purchase-info-create', kwargs={'bottle_pk': self.object.pk})

    def get_initial(self):
        return {'wine': self.kwargs['wine_pk']}


class PurchaseInfoCreateView(CreateView):
    model = models.PurchaseInfo
    form_class = forms.PurchaseInfoForm
    template_name = 'routes/purchase_info_form.html'

    def get_initial(self):
        return {'bottle': self.kwargs['bottle_pk']}

    def get_success_url(self):
        return reverse_lazy('bottle-detail', kwargs={'pk': self.object.bottle.pk})


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


class PurchaseInfoUpdateView(UpdateView):
    model = models.PurchaseInfo
    form_class = forms.PurchaseInfoForm
    template_name = 'routes/purchase_info_form.html'

    def get_success_url(self):
        return reverse_lazy('bottle-detail', kwargs={'pk': self.object.bottle.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['date'] = self.object.date
        return initial
