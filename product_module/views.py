from django.shortcuts import render, redirect, get_object_or_404

from engine.models import Module
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, permission_required

def product_list(request):
    
    module = Module.objects.get(name="product_module")
    if not module.installed:
        return redirect('module-list')

    products = Product.objects.all()
    role = 'public'

    if request.user.is_authenticated:
        groups = request.user.groups.values_list('name', flat=True)
        if 'manager' in groups:
            role = 'manager'
        elif 'user' in groups:
            role = 'user'
        elif 'public' in groups:
            role = 'public'

    return render(request, 'product_module/product_list.html', {
        'products': products,
        'role': role,
    })

# Create
@login_required
@permission_required('product_module.add_product', raise_exception=True)
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    return render(request, 'product_module/product_form.html', {'form': form})

# Update
@login_required
@permission_required('product_module.change_product', raise_exception=True)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    return render(request, 'product_module/product_form.html', {'form': form})

# Delete
@login_required
@permission_required('product_module.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'product_module/product_confirm_delete.html', {'product': product})