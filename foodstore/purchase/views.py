from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart
from .forms import CreatePayment
from django.contrib.auth.decorators import login_required
from collections import Counter
# Create your views here.
@login_required(login_url="accounts:login")
def cart_view(request,product_id):
    chosen_product = Cart()
    product = Product.objects.get(pk=product_id)
    chosen_product.chosen_productname =  product.productname
    chosen_product.chosen_price =  product.price
    chosen_product.save()
    return redirect('purchase:list')



@login_required(login_url="accounts:login")
def list_view(request):
    products = Cart.objects.all()
    total = sum([product.chosen_price for product in products])
    d= {}
    list1 = [product.chosen_productname for product in products]
    list_set = set(list1)
    unique_list = (list(list_set))
    for pro_name in unique_list:
        d[pro_name] = Counter([product.chosen_productname for product in products])[pro_name]
    return render(request,'purchase/cart.html',{'products':products,'total':total,'total_items':len(products),'d':d})

@login_required(login_url="accounts:login")
def delete_view(request,pk):
    product = Cart.objects.get(pk=pk)
    product.delete() 
    return redirect("purchase:list")

@login_required(login_url="accounts:login")
def payment_view(request):
    if request.method=="POST":
        form = CreatePayment(request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchase:success")
    else:
        form = CreatePayment()
    return render(request,'purchase/payment.html',{"form":form})

@login_required(login_url="accounts:login")
def success_view(request):
    products = Cart.objects.all()
    total = sum([product.chosen_price for product in products])
    for product in products:
        product.delete()
    return render(request,'purchase/success.html',{'total':total})