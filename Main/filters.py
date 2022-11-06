import django_filters
from django_filters import DateFilter

from .models import *

class arFilter(django_filters.FilterSet):
    class Meta:
        model = AR
        fields = ['db', 'customer', 'city', 'phone',]
        #exclude = ['location_id', 'db', 'unit_price', 'extended', 'foreign_extended', 'tax', 'cogs_extended', 'debit', 'credit',]

class partieFilter(django_filters.FilterSet):
    class Meta:
        model = Parties
        fields = ['name', 'type', 'city', 'state',]

class purchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchases
        fields = ['db', 'supplier', 'item', 'quantity',]

class saleFilter(django_filters.FilterSet):
    class Meta:
        model = Sales
        fields = ['customer', 'tdate', 'item','quantity',]
        #exclude = ['location_id', 'db', 'unit_price', 'extended', 'foreign_extended', 'tax', 'cogs_extended', 'debit', 'credit',]