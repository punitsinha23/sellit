from django.shortcuts import render, redirect, get_object_or_404
from product import models
from django.contrib.auth.decorators import login_required
from product.models import Product , Buying , Wallet
from django.contrib import messages


def home(request):
   
    products = models.Product.objects.all()
  
    return render(request , 'home_app/home.html' , {'products':products} )

@login_required
def user_home(request , username ):
    if request.user.username != username:
        return redirect('login')
    products = models.Product.objects.all()
    context = {
        'user': request.user,
        'products':products
    }
   
  
    return render(request , 'home_app/user_home.html' , context )

@login_required
def checkout_product(request, username, pk):
    if request.user.username != username:
        return redirect('login')

   
    product = get_object_or_404(models.Product, pk=pk)

    return render(request, 'home_app/checkout_product.html', {'product': product, 'username': username})

def buying(request, pk, username):
    product = get_object_or_404(Product, pk=pk)
    wallet = request.user.wallet  

    if wallet.balance >= product.price:  
        buying, created = Buying.objects.get_or_create(user=request.user)

        if not buying.products.filter(id=product.id).exists():  
            buying.products.add(product)
            wallet.balance -= product.price 
            wallet.save()  

            messages.success(request, f"You bought {product.name}! Remaining balance: {wallet.balance}")
        else:
            messages.info(request, "You already own this product.")
    else:
        messages.error(request, "Insufficient balance to buy this product!")

    return redirect(request.META.get('HTTP_REFERER', 'home'))