from django.shortcuts import render, redirect, get_object_or_404
from product import models
from django.contrib.auth.decorators import login_required


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

