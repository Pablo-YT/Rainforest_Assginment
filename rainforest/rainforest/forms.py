from django.forms import ModelForm 
from .models import Product
from django import forms

class product_form(forms.ModelForm):
	class meta:
		model = Product
		fields = ['name', 'description', 'price']

