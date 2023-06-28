from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from .models import Product,Cart,CartItem,Order,OrderItem
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm,UserRegistrationForm
# Create your views here.
User=get_user_model()

def home(request):
    return render(request,'ProductApp/home.html')

def userLogin(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print('Username:', username)
            print('Password:', password)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request,user)
           return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def userLogout(request):
    logout(request)
    return redirect('home/')  


class ProductList(ListView):
    model=Product
    template_name='product_list.html'
    context_object_name='product_view'

@login_required
def profile_view(request):
    user=request.user
    cart_items=CartItem.objects.filter(cart__user=user)
    context={
        'user':user,
        'cart_items':cart_items
    }
           
        
    return render(request,'ProductApp/profile.html',context)

@login_required
def add_to_cart(request,product_id):
    user=request.user
    product=Product.objects.get(id=product_id)

    try:
        cart=Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user)

    try:
        cart_item=CartItem.objects.get(cart=cart,product=product)
        cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart=cart,product=product,quantity=1)
    return redirect('profile')

@login_required
def order_view(request):
    user=request.user
    cart=user.cart
    total_price =sum(cart_item.product.Price * cart_item.quantity for cart_item in cart.cartitem_set.all())
    print("Total Price:", total_price)
    order=Order.objects.create(user=user,total_price=total_price)
    for cart_item in cart.cartitem_set.all():
        product = cart_item.product
        quantity_to_buy = cart_item.quantity
        if product.Quantity >= quantity_to_buy:
            product.Quantity -= quantity_to_buy
            product.save()
            OrderItem.objects.create(order=order, product=product, quantity=quantity_to_buy)
    
        # OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
    
    cart.cartitem_set.all().delete()
    order=Order.objects.create(user=user,total_price=total_price)
    context = {
        'total_price': total_price,
        'order':order
    }
    return render(request,'ProductApp/order.html',context)

@login_required
def order_success(request,total_price):
    context={
        'total_price':total_price
    }
    return render(request, 'ProductApp/order_success.html',context)

@login_required
def cart_delete(request,cart_item_id):
    cart_item=get_object_or_404(CartItem,id=cart_item_id)
    if cart_item.cart.user != request.user:
        return redirect('profile')
    cart_item.delete()
    return redirect('profile')