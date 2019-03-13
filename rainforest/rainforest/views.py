from django.urls import path
from django.shortcuts import render, get_object_or_404
from rainforest.models import Product, Review
from django.http import HttpResponseRedirect, HttpResponse
from .forms import product_form, ReviewForm


def products(request):
	product = Product.objects.all()
	context = {'product': product}
	return render(request, 'products.html', context)


def products_show(request, id):
	product = Product.objects.get(pk=id)
	reviews = product.reviews.all()
	if request.method == 'POST':
		review_form = ReviewForm(request.POST)
		if review_form.is_valid():
			new_review = review_form.save()
			return HttpResponseRedirect('/products/{}'.format(id))
		else:
			# maybe have to add form errors
			pass
	else:
		review_form = ReviewForm(initial={'product': id})
	context = {
		'product': product,
		'reviews': reviews,
		'review_form': review_form
	}
	return render(request, 'product.html', context)

def edit_review(request, id):
	review = Review.objects.get(pk=id)
	form = ReviewForm(request.POST or None, instance=review)
	if form.is_valid():
		review = form.save(commit=False)
		review.save()
		return HttpResponseRedirect('/products/')
	return render(request, 'edit_review.html', {
		'form': form,
		'review': review
	})

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

def product_review(request, id):
	product = Product.objects.get(pk=id)
	if request.method == 'POST':
		review_form = ReviewForm(request.POST)
		if review_form.is_valid():
			new_review = review_form.save()
			return HttpResponseRedirect('/products/')
		else:
			# maybe have to add form errors
			pass
	else:
		review_form = ReviewForm(initial={'product': id})
	context = {
		'review_form': review_form,
		'product': product
		}
	response = render(request, 'review.html', context)
	return HttpResponse(response)
# DONT NEED THIS FUNCTION BUT DONT KNOW HWO TO DELETE IT
def delete_review(request, id):
	review = Review.objects.get(pk=id)
	review_form = ReviewForm(request.POST or None, instance=review)
	review.delete()
	context = {
		'review_form': review_form,
		'review': review
		}
	return HttpResponseRedirect('/products/')
