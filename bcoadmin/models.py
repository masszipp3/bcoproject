from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250,null=True)
    category_description = models.CharField(max_length=250,null=True)
    category_code = models.CharField(max_length=250,unique=True,db_index=True)
    slug = models.CharField(max_length=300,null=True,blank=True)
    category_image = models.ImageField(upload_to="category_image/",null=True,blank=True)



class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=250,null=True)
    category_code = models.CharField(max_length=250,unique=True,db_index=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='',null=True,blank=True)
    slug = models.CharField(max_length=300,null=True)

class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=250,null=True)
    supplier_phone = models.CharField(max_length=250,null=True)
    supplier_city = models.CharField(max_length=250,null=True)
    supplier_code = models.CharField(max_length=250,unique=True,db_index=True)
    added_date = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
    product_name = models.CharField(max_length=250,null=True)
    product_code = models.CharField(max_length=250,unique=True,db_index=True)
    product_description = models.CharField(max_length=250,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    sub_category = models.ForeignKey(Subcategory,on_delete=models.CASCADE,default='',null=True,blank=True)
    Added = models.CharField(max_length=250,default='Admin')
    defaul_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100,default='onstock')
    added_date = models.DateTimeField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=3, default=1.000)
    min_quantity = models.DecimalField(max_digits=6, decimal_places=3, default=1.000)
    UNIT_CHOICES = (
        ('kg', 'Kilogram'),
        ('nos', 'Number'),
        ('litre', 'Litre'),
    )
    unit_type = models.CharField(null=True,max_length=20, choices=UNIT_CHOICES,blank=True)
    product_image = models.ImageField(upload_to="product_image",null=True,blank=True)

class Customer(models.Model):
    customer_name  = models.CharField('Customer Name', max_length=64,null=True)
    contact_number = models.CharField(max_length=20,null=True)
    customer_city = models.CharField(max_length=200, null=True)
    customer_code = models.CharField(max_length=100,unique=True,db_index=True)

class Stock_in(models.Model):
    product_name = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    supplier = models.ForeignKey(Suppliers,on_delete=models.CASCADE,null=True) 
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_purchased = models.IntegerField(default=1)
    stockin_date_and_time = models.DateTimeField(auto_now_add=True)

class StockReturn(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    return_quantity = models.IntegerField(default=1)
    return_reason = models.TextField()
    return_date_and_time = models.DateTimeField(auto_now_add=True)    

class Stock_out(models.Model):
    product_name = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True) 
    quantity_out = models.IntegerField(default=1)
    stockout_date_and_time = models.DateTimeField(auto_now_add=True)
    stock_return = models.ForeignKey(StockReturn, on_delete=models.CASCADE, null=True, blank=True)



    



       









        