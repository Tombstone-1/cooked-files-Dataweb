from django.db import models

class AR(models.Model):
    db = models.CharField(max_length=50, default="none")
    customer = models.CharField(max_length=100, default="none")
    invoice_amt = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    receipt_amt = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    balance = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    address = models.CharField(max_length=150, default="none")
    city = models.CharField(max_length=50, default="none")
    state = models.CharField(max_length=50, default="none")
    phone = models.CharField(max_length=150, default="none")
    email = models.CharField(max_length=250, default="none")

    def __str__(self):
        return self.db

    class Meta:
        verbose_name = 'AR List'


class Parties(models.Model):

    # specifying choices for parties table (type)
    TYPE_CHOICES = (
        ("supplier", "Supplier"),  # "actual value", "human read name"
        ("customer", "Customer"),
        ("location", "Location"),
    )

    db = models.CharField(max_length=50, default="none")
    name = models.CharField(max_length=50, default="none")
    type = models. CharField(max_length=20, choices=TYPE_CHOICES, default="none")
    address = models.CharField(max_length=150, default="none")
    address_2 = models.CharField(max_length=150, default="none")
    city = models.CharField(max_length=20, default="none")
    state = models.CharField(max_length=20, default="none")
    zip = models.IntegerField(null=True)
    country = models.CharField(max_length=20, default="none")
    phone = models.CharField(max_length=15, default="none")
    phone2 = models.CharField(max_length=15, default="none")
    email = models.CharField(max_length=50, default="none")

    def __str__(self):
        return self.db

    class Meta:
        verbose_name = 'Parties List'

class Purchases(models.Model):
    db = models.CharField(max_length=50, default="none")
    tdate = models.CharField(max_length=50, default="none")
    supplier = models.CharField(max_length=50, default="none")
    supplier_print_name = models.CharField(max_length=50, default="none")
    item = models.CharField(max_length=250, default="none")
    quantity = models.DecimalField(decimal_places=4, max_digits=10, null=True, default="0.00")
    unit_price = models.DecimalField(decimal_places=4, max_digits=10, null=True, default="0.00")
    extended = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    fob_unit_price = models.DecimalField(decimal_places=4, max_digits=10, null=True, default="0.00")
    cogs_unit_price = models.DecimalField(decimal_places=4, max_digits=10, null=True, default="0.00")
    cogs_extended = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    debit = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    credit = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")

    def __str__(self):
        return self.db

class Sales(models.Model):
    db = models.CharField(max_length=50, default="none")
    location_id = models.IntegerField(null=True)
    tdate = models.CharField(max_length=50, default="none")
    customer = models.CharField(max_length=150, default="none")
    item = models.CharField(max_length=150, default="none")
    quantity = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    unit_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    extended = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    foreign_extended = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    tax = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    cogs_extended = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    debit = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")
    credit = models.DecimalField(decimal_places=2, max_digits=10, null=True, default="0.00")

    def __str__(self):
        return self.db

    class Meta:
        verbose_name = 'Sales List'
