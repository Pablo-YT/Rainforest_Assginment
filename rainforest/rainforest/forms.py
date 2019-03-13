
from .models import Product, Review
from django import forms

class product_form(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'price']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		widgets = { 'product': forms.HiddenInput() }
		fields = ['name', 'message', 'product']
