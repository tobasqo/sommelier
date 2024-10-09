from django.urls import path

from sommelier import views

urlpatterns = [
    path('', views.BottleListView.as_view(), name='bottle-list'),
    path('wines', views.WineCreateView.as_view(), name='wine-create'),
    path('wines/<int:pk>/update/<int:bottle_pk>', views.WineUpdateView.as_view(), name='wine-update'),
    # TODO: should use next parameter but whatever
    path('bottles/<int:wine_pk>/add', views.BottleCreateView.as_view(), name='bottle-create'),
    path('bottles/<int:pk>', views.BottleDetailView.as_view(), name='bottle-detail'),
    path('bottles/<int:pk>/update', views.BottleUpdateView.as_view(), name='bottle-update'),
    path('shop-infos/<int:bottle_pk>/add', views.ShopInfoCreateView.as_view(), name='shop-info-create'),
    path('shop-infos/<int:pk>/update', views.ShopInfoUpdateView.as_view(), name='shop-info-update'),
]
