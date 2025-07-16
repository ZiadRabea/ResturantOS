from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def home(request):
    return render(request, "index.html")

def error(request):
    return render(request, "error.html")

@login_required
def add_product(request):
    user = request.user.profile
    try:
        store = user.store
    except:
        store = None
    if not store:
        return redirect("/error")
    else:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.store = store
                myform.save()
                return redirect(f"/stores/{store.id}")
        else:
            form = ProductForm()
        
        context = {
            "Form" : form,
            "store": store
        }
        return render(request, "add_product.html", context)

def products(request, id):
    store = Store.objects.get(id=id)
    products = Product.objects.filter(store=store)
    try:
        profile = request.user.profile
        saved_products_count = Product.objects.filter(savers=profile).count()
    except:
        saved_products_count = 0
    context = {
        "products": products,
        "store" : store,
        "saved_products": False,
        "saved_products_count": saved_products_count
    }
    return render(request, "products.html", context)

@login_required
def delete_product(request, id):
    try :
        store = request.user.profile.store
    except:
        store = None
    product = Product.objects.get(id=id)

    if store and store == product.store:
        product.delete()
        return redirect(f"/stores/{store.id}")
    else:
        return redirect("/error")

@login_required    
def update_product(request, id):
    user = request.user.profile
    product = Product.objects.get(id=id)
    try: 
        store = user.store 
    except: 
        store = None

    if not (store and store == product.store):
        return redirect("/error")
    else:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.store = store
                myform.save()
                return redirect(f"/stores/{store.id}")
        else:
            form = ProductForm(instance=product)
        
        context = {
            "Form" : form,
            "store": store
        }
        return render(request, "add_product.html", context)

@login_required
def save_product(request, id):
    product = Product.objects.get(id=id)
    profile = request.user.profile

    if profile in product.savers.all():
        product.savers.remove(profile)
    else:
        product.savers.add(profile)
    
    return redirect("/products/saved")

@login_required
def saved_products(request):
    profile = request.user.profile
    products = Product.objects.filter(savers=profile)
    context = {
        "products": products,
        "saved_products": True,
    }
    return render(request, "products.html", context)

@login_required
def available_product_toggle(request, id):
    try :
        store = request.user.profile.store
    except:
        store = None
    product = Product.objects.get(id=id)

    if store and store == product.store:
        if not product.is_available:
            product.is_available = True
        else:
            product.is_available = False
        product.save()
        return redirect(f"/stores/{store.id}")
    else:
        return redirect("/error")
