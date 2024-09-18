from django.urls import path

from sommelier import views

urlpatterns = [
    path('', views.BottleListView.as_view(), name='bottle-list'),
    path('wines', views.WineCreateView.as_view(), name='wine-create'),
    # path('wines/<int:pk>', views.WineUpdateView.as_view(), name='wine-update'),
    path('bottles', views.BottleCreateView.as_view(), name='bottle-create'),
    path('bottles/<int:pk>', views.BottleDetailView.as_view(), name='bottle-detail'),
    # path('bottles/<int:pk>', views.BottleUpdateView.as_view(), name='bottle-update'),
    path('shop-infos', views.ShopInfoCreateView.as_view(), name='shop-info-create'),
    # path('shop-infos/<int:pk>', views.ShopInfoUpdateView.as_view(), name='shop-info-update'),
]
