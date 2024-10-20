from django.urls import path

from sommelier import views

urlpatterns = [
    path('', views.BottleListView.as_view(), name='bottle-list'),
    path('wines', views.WineCreateView.as_view(), name='wine-create'),
    path('wines/<int:pk>/update/<int:bottle_pk>', views.WineUpdateView.as_view(), name='wine-update'),
    path('bottles/<int:wine_pk>/add', views.BottleCreateView.as_view(), name='bottle-create'),
    path('bottles/<int:pk>', views.BottleDetailView.as_view(), name='bottle-detail'),
    path('bottles/<int:pk>/update', views.BottleUpdateView.as_view(), name='bottle-update'),
    path('purchases/<int:bottle_pk>/add', views.PurchaseInfoCreateView.as_view(), name='purchase-info-create'),
    path('purchases/<int:pk>/update', views.PurchaseInfoUpdateView.as_view(), name='purchase-info-update'),
]
