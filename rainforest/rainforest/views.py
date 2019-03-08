from django.urls import path
from django.shortcuts import render
from rainforest.models import Product
from django.http import HttpResponseRedirect
from .forms import product_form


def products(request):
	context = {'products': Product.objects.all()}
	return render(request, 'products.html', context)


def products_show(request, id):
	product = Product.objects.get(pk=id)
	context = {'product': product}
	return render(request, 'product.html', context)

def root(request):
	return HttpResponseRedirect('products')


def product_create(request):
	form = product_form(request.POST or None)
	if form.is_valid():
		form.save()
	context = {'form':form}
	return render(request, 'product_create.html', context)

def create_product(request):
	product_name = request.POST['product_name']
	product_description = request.POST['product_description']
	product_price = float(request.POST['product_price'])
	new_product = Product.objects.create(name=product_name, description=product_description, price=product_price)
	return HttpResponseRedirect('/products/')
