"""MMAK_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from Supervisor.views import *

# Adding router based urls
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'Transactions', TransactionsViewSet, basename='Transaction')
router.register(r'TransactionTrackers', TransactionTrackerViewSet, basename='TransactionTracker')
router.register(r'TransactionDetails', TransactionDetailViewSet, basename='TransactionDetail')
router.register(r'Products', ProductViewSet, basename='Product')
router.register(r'DealerCust', DealerCustViewSet, basename='DealerCust')
router.register(r'Categories', CategoriesViewSet, basename='Categorie')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/Sales/<int:day>/<int:month>/<int:year>/' , view_specific_transactions , name = 'Get specific transactions'),
    path('transactions/Purchases/<int:day>/<int:month>/<int:year>/',view_specific_transactions_purchases , name = "View Purchase transactions"),
    path('transactionDetails/<int:id>/' , view_transactions_details , name = 'View transaction details'),
    path('credits/<int:day>/<int:month>/<int:year>/' ,view_credited_transactions_date_specific , name = "Vew credits based on date" ),
    path('credits/' , view_credited_transactions , name = "View all credited transactions"),
    path('transactiontracker/<int:id>/' , view_transactiontracker , name = "View transaction tracks"),
    path('searchProduct/<str:keywords>/' , search_products , name = "Search products"),
    path('searchCategory/<str:keywords>/' , search_categories , name = "Search Category"),

    path('createUser/' , create_user , name = 'Create new user'),
    path('updateUser/' , update_user , name = 'Update user'),
    path('deleteUser/<str:name>/', delete_user , name = 'Delete user'),

    path('createTransaction/' , create_transaction , name = 'Create new transaction'),
    path('updatetransaction/<str:id>/<str:Return_amount>/<str:Paid_amount>/<str:cleared>/' , updateTransaction , name = 'Update transaction'),
    path('createdetail/' , createdetails , name = 'Create detail'),
    path ('createtrack/<str:id>/<str:paid_amount>/<str:updated_by>/' , createtrack , name = "create new track"),

    path('createCategory/' ,createCategory , name = "Create new category"),
    path('updateCategory/', update_category , name = "Update a category"),
    path('deleteCategory/<str:Category>/', delete_category , name = "Delete category"),

    path('createCust/', createCust , name = "Create a customer"),
    path('updateCust/' , update_cust , name = "Update a customer"),
    path('deleteCust/<str:name>/' , Cust_delete , name = "Delete customer"),

    path('createproduct/' , createProduct , name = "Create product"),
    path('updateProduct/', updateProduct , name = "Update a product"),
    path('deleteproduct/<str:product>/' , deleteProduct , name = "Delete a product"),
    path('updateQuantity/<str:name>/<str:quantity>/', updateQuantity , name = "Update a product quantity"),
    path('BatchUpload/' , batchuploadProducts , name = "Batch Upload products"),

]


urlpatterns += router.urls
