# for APIs only
from django.urls import path
from .import views

app_name = 'Main'
urlpatterns = [
    path('ar', views.ar_view, name="ar_details"),
    path('purchase', views.purchase_view, name="purchase_details"),
    path('sales', views.sales_view, name="sale_details"),
    path('parties', views.sales_view, name="party_details"),
    
]