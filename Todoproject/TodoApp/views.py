from django.shortcuts import render
from .models import Product
# Create your views here.
def Home(request):
    data=Product.objects.all()
    return render(request,'index.html',{'data':data})



def Details(req,id):
    data=Product.objects.get(id=id)
    return render(req,'details.html',{'data':data})
