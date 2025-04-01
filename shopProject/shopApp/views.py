from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products" : products})

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        try:
            price = int(price)
        except ValueError:
            price = 0  

        Product.objects.create(
            name=name,
            description=description,
            price=price
        )
        return redirect('/shop')  # 홈으로 리디렉션

    return render(request, 'create.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'detail.html', {'product': product})

def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')

        try:
            product.price = int(product.price)
        except ValueError:
            product.price = 0

        product.save()
        return redirect(f'/shop/{product.id}/')

    return render(request, 'edit.html', {'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('/shop')


    return redirect(f'/shop/{product.id}/')
