from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"

class TransactiontrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTracker
        fields = "__all__"

class TransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransactionDetails
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class DealerCustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealercust
        fields = "__all__"

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"