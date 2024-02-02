from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('search/', views.search_product, name='search-product'),
    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productdetail, name='product_detail'),
]
