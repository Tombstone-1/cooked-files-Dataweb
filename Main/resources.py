from import_export import resources
from .models import *

class AR_resource(resources.ModelResource):
    class Meta:
        model = AR


class Parties_resource(resources.ModelResource):
    class Meta:
        model = Parties

class Purchase_resource(resources.ModelResource):
    class Meta:
        model = Purchases


class Sale_resource(resources.ModelResource):
    class Meta:
        model = Sales
