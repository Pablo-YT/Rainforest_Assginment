from django.urls import path
from django.shortcuts import render
from rainforest.models import Product


def products(request):
	context = {'products': Product.objects.all()}
	return render(request, 'products.html', context)
	

def products_show(request, id):
	product = Product.objects.all(pk=id)
	context = {'products': product}
	return render(request, 'products.html', context)