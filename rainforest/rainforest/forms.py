
from .models import Product
from django import forms

class product_form(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'price']
