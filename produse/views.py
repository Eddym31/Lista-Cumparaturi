from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from .forms import ProductsForm


def home(request):
    """
    This view function handles the main page of the web application. When the user sends a POST request, it creates a new form instance with the data submitted by the user, checks if the form is valid, saves the form data into the database, and then creates a new empty form instance and sends the form and all the products in the database to the home template. When the user sends a GET request, it creates a new empty form instance and sends the form and all the products in the database to the home template.
    """
    if request.method == 'POST':
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            products = Products.objects.all()
            context = {'form': form, 'products':products}
            return render(request, 'produse/home.html', context)
    else:
        form = ProductsForm()
        products = Products.objects.all()
        context = {'form': form, 'products': products}
        return render(request, 'produse/home.html', context)

def delete(request, id):
    """
    This view function handles the deletion of a specific product. It retrieves the product instance with the given id from the database and deletes it. It then redirects the user to the home page.
    """
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

def change_status(request, id):
    """
    This view function handles the changing of a product's status (purchased or not). It retrieves the product instance with the given id from the database and toggles its `cumparat` (purchased) boolean attribute. It then saves the updated instance and redirects the user to the home page.
    """
    product = Products.objects.get(pk=id)
    if product.cumparat:
        product.cumparat = False
        product.save()
    else:
        product.cumparat = True
        product.save()

    return redirect('home')

def about(request):
    """
    This view function handles the "about" page of the web application. It renders the about template.
    """
    return render(request, 'produse/about.html')
