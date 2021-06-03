from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProduct
from django.contrib.auth.decorators import login_required

def home_view(request):
    products = Product.objects.all()
    return render(request,'products/home.html',{'products':products})

@login_required(login_url="accounts:login")
def create_view(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form =  CreateProduct(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products:home')
        else:
            form = CreateProduct()
        return render(request,'products/create.html',{'form':form})
    else:
        return redirect("products:home")

@login_required(login_url="accounts:login")
def delete_view(request,pk):
    if request.user.is_superuser:
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('products:home')
    else:
        return redirect("products:home")

def detail_view(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/detail.html',{'product':product})