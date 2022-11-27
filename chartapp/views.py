from django.shortcuts import render, redirect
from . models import Product
from . forms import ProductForm
from django.http import HttpResponse
# Create your views here.



def add(request, article_id):
    a = Product(category="Ttest1", num_of_products=int(article_id))
    a.save()
    return HttpResponse(article_id)

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }

    return render(request, 'chartapp/index.html', context)
