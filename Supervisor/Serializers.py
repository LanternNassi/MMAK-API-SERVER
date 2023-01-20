from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
    def create(self,validated_data):
        created_user = Users(**validated_data)
        created_user.save()
        return created_user
    def update(self,instance,validated_data):
        instance.user = validated_data.get('user' , instance.user)
        instance.contact = validated_data.get('contact' , instance.contact)
        instance.gender = validated_data.get('gender' , instance.gender)
        instance.type = validated_data.get('type',instance.type)
        instance.save()
        return instance

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"
    def create(self , validated_data):
        
        newtransaction = Transactions(**validated_data)
        newtransaction.save()
        return newtransaction
    def update(self,instance,validated_data):
        instance.type = validated_data.get('type' , instance.type)
        instance.dea_cust_name = validated_data.get('dea_cust_name' , instance.dea_cust_name)
        instance.grandtotal = validated_data.get('grandtotal' , instance.grandtotal)
        instance.transaction_date = validated_data.get('transaction_date' , instance.transaction_date)
        instance.discount = validated_data.get('discount' , instance.discount)
        instance.added_by = validated_data.get('added_by' , instance.added_by)
        instance.paid_amount = validated_data.get('paid_amount' , instance.paid_amount)
        instance.return_amount = validated_data.get('return_amount' , instance.return_amount)
        instance.total_profit = validated_data.get('total_profit' , instance.total_profit)
        instance.paid = validated_data.get('paid' , instance.paid)
        instance.taken = validated_data.get('paid_amount' , instance.taken)
        instance.save()
        return instance

class TransactiontrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTracker
        fields = "__all__"
    def create(self,validated_data):
        newtrack = TransactionTracker(**validated_data)
        newtrack.save()
        return newtrack

class TransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransactionDetails
        fields = "__all__"
    def create(self,validated_data):
        new_detail = TransactionDetails(**validated_data)
        new_detail.save()
        return new_detail

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
    def create(self,validated_data):
        new_product = Products(**validated_data)
        new_product.save()
        return new_product
    def update(self,instance,validated_data):
        instance.product = validated_data.get('product' , instance.product)
        instance.category = validated_data.get('category' , instance.category)
        instance.description = validated_data.get('description',instance.description)
        instance.rate = validated_data.get('rate' , instance.rate)
        instance.selling_price = validated_data.get('selling_price' , instance.selling_price)
        instance.quantity = validated_data.get('quantity' , instance.quantity)
        instance.added_date = validated_data.get('added_date' , instance.added_date)
        instance.added_by = validated_data.get('added_by' , instance.added_by)
        instance.save()
        return instance

class DealerCustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealercust
        fields = "__all__"
    def create(self,validated_data):
        new_cust = Dealercust(**validated_data)
        new_cust.save()
        return new_cust
    def update(self,instance,validated_data):
        instance.type = validated_data.get('type',instance.type)
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email' , instance.email)
        instance.contact = validated_data.get('contact' , instance.contact)
        instance.address = validated_data.get('address' , instance.address)
        instance.added_date = validated_data.get('added_date' , instance.added_date) 
        instance.added_by = validated_data.get('added_by' , instance.added_by)
        instance.save()
        return instance

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
    def create(self,validated_data):
        new_category = Categories(**validated_data)
        new_category.save()
        return new_category
    def update(self , instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.description = validated_data.get('description' , instance.description)
        instance.added_date = validated_data.get('added_date' , instance.added_date)
        instance.added_by = validated_data.get('added_by' , instance.added_by)
        instance.save()
        return instance