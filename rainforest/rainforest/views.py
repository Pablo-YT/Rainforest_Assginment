from django.urls import path
from django.shortcuts import render, get_object_or_404
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
	context = {'form':form}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/products/')
	else:
		return render(request, 'product_create.html', context)

def product_delete(request, id):
	product = Product.objects.get(pk=id)
	if request.method == 'POST':
		product.delete()
		return HttpResponseRedirect('/products/')
	context = {
		'product': product
	}
	return render(request, 'product_delete.html', context)
