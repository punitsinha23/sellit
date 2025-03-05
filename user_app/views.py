from django.shortcuts import render, redirect , get_object_or_404
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from product.models import Product , Cart , Wallet , Buying

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Wallet.objects.create(user=user)
            login(request, user)
            messages.success(request, f'Signup successful! Welcome {user.username}')
            return redirect(reverse('profile', kwargs={'username': user.username}))

    else:
        form = SignupForm()

    return render(request, 'user_app/signup.html', {"form": form})


def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user) 
                    messages.success(request, 'You have successfully logged in')
                    return redirect('profile', user.username)
                else:
                    messages.error(request, 'Invalid email or password.')
            except User.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')
        else:
            messages.error(request, 'Invalid form submission.')

    else:
        form = LoginForm()

    return render(request, 'user_app/login.html', {'form': form})

@login_required(login_url='login')
def user_dashboard(request, username):
    if request.user.username != username:
        return redirect('login') 

    count = Product.objects.filter(user=request.user).count()
    cart = Cart.objects.filter(user=request.user).count()

   
    try:
        buying = Buying.objects.get(user=request.user)  
        product_count = buying.products.count()  
    except Buying.DoesNotExist:
        product_count = 0  

    context = {
        'username': username,
        'user': request.user,
        'count': count,
        'cart': cart,
        'product_count': product_count, 
    } 
    return render(request, 'user_app/user.html', context)


    
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  


@login_required
def buying_list(request, username):
    buying = get_object_or_404(Buying, user=request.user)  
    products = buying.products.all()

    return render(request, 'user_app/buying_list.html', {'products': products})
