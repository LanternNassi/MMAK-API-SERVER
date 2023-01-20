from django.shortcuts import render
from .Serializers import *
from .models import *
from rest_framework import viewsets , permissions , status
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


#===========================================The winforms app side views(Majorly POST,DELETE,UPDATE requests)==============================


# Users views 
@api_view(['POST'])
@permission_classes([])
def create_user(request):
    # print(request.data)
    # return Response(data={'success':1} , status = status.HTTP_201_CREATED)
    serialized_user = UserSerializer(data=request.data)
    if (serialized_user.is_valid()):
        created_user = serialized_user.create(serialized_user.validated_data)
        return Response(data = UserSerializer(created_user).data , status = status.HTTP_201_CREATED)
    else :
        return Response(data = serialized_user.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([])
def update_user(request):
    serialized_user = UserSerializer(data=request.data)
    User = Users.objects.get(id = request.data['id'])
    if (serialized_user.is_valid()):
        created_user = serialized_user.update(User,serialized_user.validated_data)
        return Response(data = UserSerializer(created_user).data , status = status.HTTP_202_ACCEPTED)
    else :
        return Response(data = serialized_user.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([])
def delete_user(request,name):
    User = Users.objects.get(id = name)
    User.delete()
    return Response(data={'id':User.id} , status=status.HTTP_200_OK)

#=============Transactions========================================
@api_view(['POST'])
@permission_classes([])
def create_transaction(request):
    processed_obj = {
        'type' : request.data['Type'],
        'dea_cust_name' : request.data['Dea_Cust_name'],
        'grandtotal':request.data['GrandTotal'],
        'transaction_date' : request.data['Transaction_date'],
        'discount' : request.data['Discount'],
        'added_by' : request.data['Added_by'],
        'paid_amount' : request.data['Paid_amount'],
        'return_amount' : request.data['Return_amount'],
        'total_profit' : request.data['Total_Profit'],
        'paid' : request.data['Paid'],
        'taken' : request.data['Taken'],
    }
    serialized_transaction = TransactionsSerializer(data = processed_obj)
    if (serialized_transaction.is_valid()):
        new_transaction = serialized_transaction.create(serialized_transaction.validated_data)
        return Response(data = TransactionsSerializer(new_transaction).data , status = status.HTTP_201_CREATED)
    else :
        return Response(data = serialized_transaction.error_messages , status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['PUT'])
# @permission_classes([])
# def update_transaction(request,id):
#     # transaction = Transactions.objects.get(id = id)
#     # serialized_transaction  = TransactionsSerializer(data = request.data)
#     # if (serialized_transaction.is_valid()):
#     #     updated_transaction = serialized_transaction.update(transaction , serialized_transaction.validated_data)
#     #     return Response(data=TransactionsSerializer(update_transaction).data , status = status.HTTP_202_ACCEPTED)
#     # else : 
#     #     return Response(data=serialized_transaction.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([])
def createdetails(request):
    processed_obj = {
        'product_name' : request.data['Product_name'],
        'rate' : request.data['Rate'],
        'qty' : request.data['qty'],
        'total' : request.data['Total'],
        'dea_cust_name' : request.data['Dea_Cust_name'],
        'added_date' : request.data['Added_date'],
        'added_by' : request.data['Added_by'],
        'invoice_id' : request.data['invoice_id'],
        'profit' : request.data['profit'],
    }
    serializedtransaction = TransactionDetailsSerializer(data = processed_obj)
    if (serializedtransaction.is_valid()):
        new_detail = serializedtransaction.create(serializedtransaction.validated_data)
        return Response(data = TransactionDetailsSerializer(new_detail).data , status = status.HTTP_201_CREATED)
    else :
        return Response(data = serializedtransaction.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([])
def createtrack(request,id , paid_amount ,updated_by):
    processed_obj = {
        'transaction_id' : id,
        'paid_amount' : paid_amount,
        'added_date' : datetime.datetime.now(),
        'updated_by': updated_by,
    }
    serialized_track = TransactiontrackerSerializer(data = processed_obj)
    if (serialized_track.is_valid()):
        newtrack = serialized_track.create(serialized_track.validated_data)
        return Response(data = TransactiontrackerSerializer(newtrack).data,status=status.HTTP_201_CREATED)
    else :
        return Response(data = serialized_track.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([])
def updateTransaction(request , id , Return_amount , Paid_amount , cleared):
    # return Response(data={} , status = status.HTTP_200_OK)
    transaction = Transactions.objects.get(id = id)
    serialized_transaction1 = TransactionsSerializer(transaction)
    processed_obj = {
        **serialized_transaction1.data,
        'return_amount' : Return_amount,
        'paid_amount' : Paid_amount,
        'paid' : 'Cleared' if (cleared or (cleared == 'true')) else False,
    }
    serialized_transaction = TransactionsSerializer(data = processed_obj)
    if (serialized_transaction.is_valid()):
        updated_transaction = serialized_transaction.update(transaction , serialized_transaction.data)
        return Response(data = TransactionsSerializer(updated_transaction).data , status = status.HTTP_202_ACCEPTED)
    else :
        return Response(data = serialized_transaction.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

#=============================views for Categories ==========================================

@api_view(['POST'])
@permission_classes([])
def createCategory(request):
    processed_obj = {
        'title' : request.data['Title'],
        'description' : request.data['Description'],
        'added_date' : datetime.datetime.now(),
        'added_by' : request.data['Added_by']
    }
    serialized_category = CategoriesSerializer(data=processed_obj)
    if (serialized_category.is_valid()):
        created_user = serialized_category.create(serialized_category.validated_data)
        return Response(data = CategoriesSerializer(created_user).data , status = status.HTTP_201_CREATED)
    else :
        return Response(data = serialized_category.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([])
def update_category(request):
    category = Categories.objects.get(id = request.data['ID'])
    processed_obj = {
        'title' : request.data['Title'],
        'description' : request.data['Description'],
        'added_date' : category.added_date,
        'added_by' : request.data['Added_by']
    }
    serialized_category = CategoriesSerializer(data=processed_obj)
    if (serialized_category.is_valid()):
        created_user = serialized_category.update(category,serialized_category.validated_data)
        return Response(data = CategoriesSerializer(created_user).data , status = status.HTTP_202_ACCEPTED)
    else :
        return Response(data = serialized_category.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([])
def delete_category(request,Category):
    Category = Categories.objects.get(id = Category)
    Category.delete()
    return Response(data={'id':Category.id} , status=status.HTTP_200_OK)



#=========================Dealers and Customers================================

@api_view(['POST'])
@permission_classes([])
def createCust(request):
    processed_obj = {
        'type' : request.data['Type'],
        'name' : request.data['Name'],
        'email' : request.data['Email'],
        'contact' : request.data['Contact'],
        'address' : request.data['Address'],
        'added_date' : datetime.datetime.now(),
        'added_by' : request.data['Added_by'],
    }
    serialized_cust = DealerCustSerializer(data = processed_obj)
    if (serialized_cust.is_valid()):
        new_cust = serialized_cust.create(serialized_cust.validated_data)
        return Response(data=DealerCustSerializer(new_cust).data , status = status.HTTP_201_CREATED)
    else:
        return Response(data=serialized_cust.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([])
def update_cust(request):
    Cust_instance = Dealercust.objects.get(id = request.data['Id'])
    processed_obj = {
        'type' : request.data['Type'],
        'name' : request.data['Name'],
        'email' : request.data['Email'],
        'contact' : request.data['Contact'],
        'address' : request.data['Address'],
        'added_date' : Cust_instance.added_date,
        'added_by' : request.data['Added_by'],
    }
    serialized_cust = DealerCustSerializer(data = processed_obj)
    if (serialized_cust.is_valid()):
        updated_cust = serialized_cust.update(Cust_instance , serialized_cust.validated_data)
        return Response(data=DealerCustSerializer(updated_cust).data , status = status.HTTP_202_ACCEPTED)
    else :
        return Response(data = serialized_cust.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['DELETE'])
@permission_classes([])
def Cust_delete(request , name):
    cust = Dealercust.objects.get(id = name)
    cust.delete()
    return Response(data=DealerCustSerializer(cust).data , status = status.HTTP_200_OK)


# =========================Products ============================================

@api_view(['POST'])
@permission_classes([])
def createProduct(request):
    processed_obj = {
        'product' : request.data['products'],
        'category' : request.data['Category'],
        'description' : request.data['Description'],
        'rate' : request.data['Rate'],
        'selling_price' : request.data['Selling_price'],
        'quantity' : request.data['Quantity'],
        'added_date' : datetime.datetime.now(),
        'added_by' : request.data['Added_by'],
    }
    serialized_product = ProductSerializer(data = processed_obj)
    if (serialized_product.is_valid()):
        new_product = serialized_product.create(serialized_product.validated_data)
        return Response(data = serialized_product.validated_data , status = status.HTTP_201_CREATED)
    else :
        return Response(data = serialized_product.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([])
def updateProduct(request):
    product = Products.objects.get(id=request.data['Id'])
    processed_obj = {
        'product' : request.data['products'],
        'category' : request.data['Category'],
        'description' : request.data['Description'],
        'rate' : request.data['Rate'],
        'selling_price' : request.data['Selling_price'],
        'quantity' : request.data['Quantity'],
        'added_date' : product.added_date,
        'added_by' : request.data['Added_by'],
    }
    serialized_product = ProductSerializer(data=processed_obj)
    if(serialized_product.is_valid()):
        updated_product = serialized_product.update(product , serialized_product.validated_data)
        return Response(data=ProductSerializer(updated_product).data , status = status.HTTP_202_ACCEPTED)
    else :
        return Response(data=serialized_product.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([])
def deleteProduct(request , product):
    product = Products.objects.get(id = product)
    product.delete()
    return Response(data=ProductSerializer(product).data , status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([])
def updateQuantity(request , name , quantity):
    product = Products.objects.get(product = name)
    product.quantity = quantity
    product.save()
    return Response(data = ProductSerializer(product).data , status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([])
def batchuploadProducts(request):
    # print(request.data)
    for product in request.data:
        processed_obj = {
            'product' : product['products'],
            'category' : product['Category'],
            'description' : product['Description'],
            'rate' : product['Rate'],
            'selling_price' : product['Selling_price'],
            'quantity' : product['Quantity'],
            'added_date' : datetime.datetime.now(),
            'added_by' : product['Added_by'],
        }
        serialized_prod = ProductSerializer(data = processed_obj)
        if(serialized_prod.is_valid()):
            new_prod = serialized_prod.create(serialized_prod.validated_data)
        else :
            return Response(data = serialized_prod.error_messages , status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(data={'success':True} , status = status.HTTP_201_CREATED)