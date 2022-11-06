from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from Main.models import *
from .serializers import *

api_view(['GET', 'POST'])
def ar_view(request):
    try:
        if request.method == 'GET':
            ar_data = AR.objects.all()
            serializer = AR_Serializer(ar_data, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = AR_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except AR.DoesNotExist:
        return Response({'message': 'Data does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def purchase_view(request):
    try:
        if request.method == 'GET':
            purchase_data = Purchases.objects.all()
            serializer = Purchases_Serializer(purchase_data, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = Purchases_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Purchases.DoesNotExist:
        return Response({'message': 'Data does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def sales_view(request):
    try:
        if request.method == 'GET':
            sales_data = Sales.objects.all()
            serializer = Sales_Serializer(sales_data, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = Sales_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Sales.DoesNotExist:
        return Response({'message': 'Data does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def parties_view(request):
    try:
        if request.method == 'GET':
            parties_data = Parties.objects.all()
            serializer = Parties_Serializer(parties_data, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = Parties_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Parties.DoesNotExist:
        return Response({'message': 'Data does not exist'}, status=status.HTTP_404_NOT_FOUND)