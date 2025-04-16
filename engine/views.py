from django.shortcuts import render, redirect
from django.http import Http404

from product_module.models import Product
from .models import Module

def dynamic_router(request, path=None):
    try:
        product_module = Module.objects.get(name='product_module')
        if product_module.installed:
            from product_module.views import product_list
            return product_list(request)
        else:
            raise Http404("Module not installed")
    except Module.DoesNotExist:
        raise Http404("Module not found")
    
def landing_page(request):
    return render(request, 'engine/landing.html')

def module_list(request):
    if request.method == "POST":
        action = request.POST.get('action')
        module_name = request.POST.get('module_name')
        module = Module.objects.get(name=module_name)

        if action == "install":
            module.installed = True
        if action == "uninstall":
            module.installed = False
        if action == "upgrade":
            upgrade_module(module_name)
        
        module.save()

        return redirect('module-list')

    modules = Module.objects.all()
    return render(request, 'engine/module_list.html', {'modules': modules})
        

def upgrade_module(module_name):
    if module_name == "product_module":
        # Jalankan makemigrations dan migrate secara otomatis
        import subprocess
        subprocess.call(["python", "manage.py", "makemigrations", module_name])
        subprocess.call(["python", "manage.py", "migrate", module_name])
        return redirect('module-list')