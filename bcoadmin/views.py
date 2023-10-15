from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from . models import *

def fetchsubcategory(request):
    cat_id=request.GET.get('catid')
    subcategories = Subcategory.objects.filter(category_id=cat_id)
    categories=[{'id': subcategory.id, 'name': subcategory.subcategory_name} for subcategory in subcategories]
    return JsonResponse({'data':categories})

# Create your views here.
class IndexView(View):
    def get(self, request):
        catagorycount=Category.objects.count()
        product=Products.objects.count()
        suppliers=Suppliers.objects.count()
        customer=Customer.objects.count()
        recent_products = Products.objects.all()
        return render(request, 'bcoadmin/index.html', {'category_count':catagorycount,'product_count':product,'suppliers_count':suppliers,'customers_count':customer,'recent_products':recent_products.order_by('-added_date')[:10]})

class addproduct(View):
    categories=Category.objects.all()
    sub_categories=Subcategory.objects.all()
    
    def get(self, request):
        return render(request, 'bcoadmin/addproducts.html', {'categories':self.categories,'choices':Products.UNIT_CHOICES})
    
    def post(self, request):
        try:
            product_obj = Products.objects.create(product_name=request.POST['product_name'],product_code=request.POST['product_code'],
                                                product_description=request.POST['product_description'],defaul_price=request.POST['product_price'],
                                                purchase_price=request.POST['product_price'],quantity=request.POST['product_quantity'],min_quantity=request.POST['product_min_quantity'],
                                                unit_type=request.POST['product_unit_type'],product_image=request.FILES['product_image'],
                                                category_id=request.POST['product_category'],sub_category_id=request.POST['product_subcategory'])
        except:
            pass    
            
        return redirect('bco_Admin:addproduct')

class addcategory(View):
    def get(self, request):
        return render(request, 'bcoadmin/addcategory.html' )
    
    def post(self, request):
        try:
            categoryobj = Category.objects.create(category_name=request.POST['category_name'],category_code=request.POST['category_code'],
                                              category_description=request.POST['category_description'],category_image=request.FILES['category_image'])
        except:
            pass
        return render(request,'bcoadmin/addcategory.html', {'data': 'Category Added Successfully'})


class addSubcategory(TemplateView):
    categories=Category.objects.all()
    def get(self, request):
        return render(request, 'bcoadmin/addsubcategory.html',{'categories':self.categories} )
    def post(self, request):
        categoryobj = Subcategory.objects.create(subcategory_name=request.POST['sub_category_name'],category_code=request.POST['sub_category_code'],category_id=request.POST['sub_category_parent'])
        return render(request,'bcoadmin/addsubcategory.html', {'data': 'Sub Category Added Successfully','categories':self.categories})


class status_out_of_stock(View):
    def get(self, request,pid):
        product= Products.objects.get(product_code=pid)
        product.status='Outofstock'
        # product.quantity=0
        product.save()
        return redirect('bco_Admin:products')

class status_stock_in(View):
    def get(self, request,pid):
        product= Products.objects.get(product_code=pid)
        product.status='onstock'
        # product.quantity=0
        product.save()
        return redirect('bco_Admin:products')
    
class product_delete(View):
    def get(self, request,pid):
        product= Products.objects.get(product_code=pid)
        product.delete()
        return redirect('bco_Admin:products')    
    
class category_delete(View):
    def get(self, request,cid):
        category= Category.objects.get(category_code=cid)
        category.delete()
        return redirect('bco_Admin:category')     
    
class sub_category_delete(View):
    def get(self, request,subcid):
        category= Subcategory.objects.get(category_code=subcid)
        category.delete()
        return redirect('bco_Admin:subcategories')      

class addCustomers(TemplateView):
    template_name = 'bcoadmin/addcustomers.html'

class addventors(TemplateView):
    template_name = 'bcoadmin/addventors.html'      

class editproduct(View):
    def get(self, request , pid ):
        product=Products.objects.filter(product_code=pid).first()
        categories=Category.objects.all()
        subcategories=Subcategory.objects.all()
        return render(request, 'bcoadmin/editproduct.html',{'categories':categories,'subcategories':subcategories,'product':product,'choices':Products.UNIT_CHOICES} )     
    def post(self,request,pid):
        product=Products.objects.filter(product_code=request.POST['product_code']).first()
        # product = 
        product.product_name=request.POST['product_name']
        product.product_code=request.POST['product_code']
        product.product_description=request.POST['product_description']
        product.defaul_price=request.POST['product_price']
        product.purchase_price=request.POST['product_price']
        product.quantity=request.POST['product_quantity']
        product.min_quantity=request.POST['product_min_quantity']
        product.unit_type=request.POST['product_unit_type']
        product.category_id=request.POST['product_category']
        product.sub_category_id=request.POST['product_subcategory']

        if request.FILES:
            product.product_image=request.FILES['product_image']
        product.save()    
        return redirect('/product/edit/'+pid)


class editcustomers(TemplateView):
    template_name = 'bcoadmin/editcustomers.html'   

class editcategory(View):
   def get(self, request,cid):
        category=Category.objects.filter(category_code = cid).first()
        # print(products)
        return render(request, 'bcoadmin/editcategory.html',{'category':category} )
   def post(self,request,cid):
       category=Category.objects.get(category_code = cid)
       category.category_name=request.POST['category_name']
       category.category_code=request.POST['category_code']
       category.category_description=request.POST['category_description']
       if request.FILES:
            category.category_image=request.FILES['category_image']
       category.save()
       return redirect('/category/edit/'+cid)    
       

class editsubcategory(View):
    def get(self, request,subcid):
        category=Subcategory.objects.get(category_code=subcid)
        categories=Category.objects.all()
        # print(products)
        return render(request, 'bcoadmin/editsubcategory.html',{'category':category,'categories':categories} )
    def post(self,request,subcid):
        category = Subcategory.objects.get(category_code=subcid)
        category.subcategory_name=request.POST['sub_category_name']
        category.category_code=request.POST['sub_category_code']
        category.category_id=request.POST['sub_category_parent']
        category.save()
        # print(category.category.id)

        return redirect('/subcategory/edit/'+subcid)

    

class editsuppliers(TemplateView):
    template_name = 'bcoadmin/editventors.html'      

class productsview(View):
     def get(self, request):
        products=Products.objects.all()
        print(products)
        return render(request, 'bcoadmin/products.html',{'products':products} )        

class categoryview(View):
    def get(self, request):
        category=Category.objects.all()
        # print(products)
        return render(request, 'bcoadmin/categories.html',{'categories':category} )          

class customersviews(TemplateView):
    template_name = 'bcoadmin/customers.html'      

class suppliersview(TemplateView):
    template_name = 'bcoadmin/ventors.html'      

class subcategoryview(TemplateView):
    def get(self, request):
        subcategory=Subcategory.objects.all()
        # print(products)
        return render(request, 'bcoadmin/subcategories.html',{'categories':subcategory} )            

class productdetailsview(View):
    def get(self, request,pid):
        product=Products.objects.filter(product_code=pid).first()
        return render(request, 'bcoadmin/productdetail.html', {'product': product})        
    
class purchasedetail(TemplateView):
    template_name = 'bcoadmin/purchasedetail.html'

class saledetailsview(TemplateView):
    template_name = 'bcoadmin/viewsale.html'                       









  


