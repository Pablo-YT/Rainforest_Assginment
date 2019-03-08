from django.urls import path
from django.shortcuts import render
from rainforest.models import Product


def products(request):
	context = {'products': Product.objects.all()}
	return render(request, 'products.html', context)
	