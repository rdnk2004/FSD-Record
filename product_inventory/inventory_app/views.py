# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    search = request.GET.get("search")
    category = request.GET.get("category")

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category_id=category)

    return render(request, "home.html", {
        "products": products,
        "categories": categories
    })

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category_id = request.POST.get("category")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            category=category,
            price=price,
            stock=stock
        )

        return redirect("add_product")

    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "add_product.html", {
        "products": products,
        "categories": categories
    })

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.name = request.POST.get("name")

        category_id = request.POST.get("category")
        product.category = Category.objects.get(id=category_id)

        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")

        product.save()

        return redirect("add_product")

    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "add_product.html", {
        "product": product,
        "products": products,
        "categories": categories,
    })

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()

    return redirect("add_product")
