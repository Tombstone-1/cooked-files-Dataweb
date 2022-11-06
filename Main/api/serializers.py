from rest_framework import serializers
from Main.models import *

class AR_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AR
        fields = '__all__'


class Purchases_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = '__all__'


class Sales_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class Parties_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = '__all__'
