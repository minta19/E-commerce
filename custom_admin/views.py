from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddUserForm, AddProductForm,AdminLoginForm,EditProductQuantityForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from ProductApp.models import Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

User = get_user_model()



@login_required(login_url='admin_login')  
def admin_login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_home')
            else:
                form.add_error(None, 'Invalid admin username or password.')
    else:
        form = AdminLoginForm()
    return render(request, 'custom_admin/admin_login.html', {'form': form})

@login_required
def admin_panel(request):
    return render(request, 'custom_admin/admin_base.html')

@login_required
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully.')
            return redirect('custom_admin:admin_home')
    else:
        form = AddUserForm()
    
    context = {
        'form': form
    }
    return render(request, 'custom_admin/adduser.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('custom_admin:admin_home')
    else:
        form = AddProductForm()
    
    context = {
        'form': form
    }
    return render(request, 'custom_admin/add_product.html', context)

def view_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'custom_admin/view_users.html', context)

def product_list_view(request):
    products = Product.objects.all()
    context={
        'products': products
    }
    return render(request, 'custom_admin/product_list.html',context)


def edit_product_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = EditProductQuantityForm(request.POST, instance=product)
        if 'Quantity' in request.POST:
           if form.is_valid():
              form.save()
              return redirect('custom_admin:prodlist')
    else:
        form = EditProductQuantityForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'custom_admin/edit_product_quantity.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('custom_admin:prodlist')
    context = {
        'product': product,
    }
    return render(request, 'custom_admin/delete_product.html', context)