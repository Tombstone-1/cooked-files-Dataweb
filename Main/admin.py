from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin

class AR_Admin(ImportExportModelAdmin):
    list_display = ('db', 'customer', 'city')


admin.site.register(AR, AR_Admin)


class Purchase_Admin(ImportExportModelAdmin):
    list_display = ('db', 'supplier', 'tdate')


admin.site.register(Purchases, Purchase_Admin)


class Sales_Admin(ImportExportModelAdmin):
    list_display = ('db', 'customer', 'tdate')


admin.site.register(Sales, Sales_Admin)


class Parties_Admin(ImportExportModelAdmin):
    list_display = ('db', 'name', 'type')


admin.site.register(Parties, Parties_Admin)