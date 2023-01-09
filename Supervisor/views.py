from django.shortcuts import render
from .Serializers import *
from .models import *
from rest_framework import viewsets , permissions
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.response import Response
import datetime


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()

class TransactionTrackerViewSet(viewsets.ModelViewSet):
    serializer_class = TransactiontrackerSerializer
    queryset = TransactionTracker.objects.all()

class TransactionDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionDetailsSerializer
    queryset = TransactionDetails.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

class DealerCustViewSet(viewsets.ModelViewSet):
    serializer_class = DealerCustSerializer
    queryset = Dealercust.objects.all()

class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

@api_view(['GET'])
@permission_classes([])
def view_specific_transactions(request,day,month,year):
    queryset = Transactions.objects.filter(
        type = "Customer",
        transaction_date__year = year,
        transaction_date__month = month,
        transaction_date__day = day
    )
    return Response(data = TransactionsSerializer(queryset , many =True).data )
  

@api_view(['GET'])
@permission_classes([])
def view_specific_transactions_purchases(request,day,month,year):
    queryset = Transactions.objects.filter(
        type = "Dealer",
        transaction_date__year = year,
        transaction_date__month = month,
        transaction_date__day = day
    )
    return Response(data = TransactionsSerializer(queryset , many =True).data )

@api_view(['GET'])
@permission_classes([])
def view_transactions_details(request, id):
    queryset = TransactionDetails.objects.filter(invoice_id = id)
    return Response(data = TransactionDetailsSerializer(queryset , many = True).data)


@api_view(['GET'])
@permission_classes([])
def view_credited_transactions_date_specific(request , day , month , year):
    queryset = Transactions.objects.filter(
        type = "Customer",
        transaction_date__year = year,
        transaction_date__month = month,
        transaction_date__day = day
    ).exclude(paid = "True")
    return Response(data = TransactionsSerializer(queryset , many =True).data )

@api_view(['GET'])
@permission_classes([])
def view_credited_transactions(request):
    queryset = Transactions.objects.filter(
        type = "Customer", 
    ).exclude(paid = "True")
    return Response(data = TransactionsSerializer(queryset , many =True).data )


@api_view(['GET'])
@permission_classes([])
def view_transactiontracker(request , id):
    queryset = TransactionTracker.objects.filter(
        transaction_id = id
    )
    return Response(data = TransactiontrackerSerializer(queryset , many=True).data)

@api_view(['GET'])
@permission_classes([])
def search_products(request,keywords):
    queryset = Products.objects.filter(product__icontains = keywords)
    return Response(data = ProductSerializer(queryset , many=True).data)

@api_view(['GET'])
@permission_classes([])
def search_categories(request,keywords):
    queryset = Categories.objects.filter(title__icontains = keywords)
    return Response(data = CategoriesSerializer(queryset , many=True).data)