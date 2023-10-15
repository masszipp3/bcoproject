from django.urls import path
from . import views

app_name='bco_Admin'

urlpatterns = [
    path('',views.IndexView.as_view(), name="home"),
    path('addproduct',views.addproduct.as_view(), name="addproduct"),
    path('addcategory',views.addcategory.as_view(), name="addcategory"),
    path('addsubcategory',views.addSubcategory.as_view(), name="addsubcategory"),
    path('addcustomer',views.addCustomers.as_view(), name="addcutomer"),
    path('addsuppliers',views.addventors.as_view(), name="addsuppliers"),
    path('product/edit/<str:pid>',views.editproduct.as_view(), name="productedit"),
    path('category/edit/<str:cid>',views.editcategory.as_view(), name="categoryedit"),
    path('subcategory/edit/<str:subcid>',views.editsubcategory.as_view(), name="subcategoryedit"),
    path('customers/edit',views.editcustomers.as_view(), name="customersedit"),
    path('suppliers/edit',views.editsuppliers.as_view(), name="supplietrsedit"),
    path('product',views.productsview.as_view(), name="products"),
    path('customers',views.customersviews.as_view(), name="customers"),
    path('suppliers',views.suppliersview.as_view(), name="suppliers"),
    path('category',views.categoryview.as_view(), name="category"),
    path('fetchsubcategory',views.fetchsubcategory, name="fetchsubcategory"),
    path('subcategories',views.subcategoryview.as_view(), name="subcategory"),
    path('product/detail/<str:pid>',views.productdetailsview.as_view(), name="productdetail"),
    path('purchase/detail',views.purchasedetail.as_view(), name="purchasedetail"),
    path('sale/detail/',views.saledetailsview.as_view(), name="saledetail"),
    path('product/<str:pid>/instock',views.status_stock_in.as_view(), name="stock_in"),
    path('product/<str:pid>/outofstock',views.status_out_of_stock.as_view(), name="out_of_stock"),
    path('product/<str:pid>/delete',views.product_delete.as_view(), name="product_delete"),
    path('category/<str:cid>/delete',views.category_delete.as_view(), name="category_delete"),
    path('subcategory/<str:subcid>/delete',views.sub_category_delete.as_view(), name="sub_category_delete"),




    





    
















]