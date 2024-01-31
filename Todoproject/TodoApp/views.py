from django.shortcuts import render,get_object_or_404
from .models import Product,Category
# Create your views here.
def Home(request,c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        print(c_page)
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True) 
           
    return render(request,'index.html',{'data':product_list,'category':c_page})



def Details(req,id):
    data=Product.objects.get(id=id)
    return render(req,'details.html',{'data':data})
