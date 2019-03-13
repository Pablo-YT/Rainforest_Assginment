from django.urls import path
from django.shortcuts import render, get_object_or_404
from rainforest.models import Product
from django.http import HttpResponseRedirect
from .forms import product_form


def products(request):
	product = Product.objects.all()
	context = {'product': product}
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

def product_edit(request, id):
	product = Product.objects.get(pk=id)
	form = product_form(request.POST or None, instance=product)
	if form.is_valid():
		product = form.save(commit=False)
		product.save()
		return HttpResponseRedirect('/products/')
	context = {
		'form': form,
		'product': product
		}
		# return HttpResponseRedirect('/products/')
	return render(request, 'product_edit.html', context)

def product_delete(request, id):
	# product = Product.objects.get(pk=id)
	# form = product_form(request.POST or None, instance=product)
	# if form.is_valid():
	# 	product = form.save(commit=False)
	# 	product.delete()
	# 	return HttpResponseRedirect('/products/')
	# context = {
	# 	'form': form,
	# 	'product': product
	# 	}
	# return render(request, 'product_delete.html', context)
	product = Product.objects.get(pk=id)
	form = product_form(request.POST or None, instance=product)
	product.delete()
	context = {
		'form': form,
		'product': product
		}
	return HttpResponseRedirect('/products/')
#
# def delete_real(request, id):
# 	product = Product.objects.get(pk=id)
# 	form = product_form(request.POST or None, instance=product)
# 	form.delete()
# 	context = {
# 		'form': form,
# 		'product': product
# 		}
# 	return HttpResponseRedirect('/products/')
