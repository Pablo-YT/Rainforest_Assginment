from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

min_length = MinLengthValidator(limit_value=10, message='Error: Description needs to be atleast 10 characters long')

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=500, validators=[min_length])
	price = models.CharField(max_length=255)


	def __str__(self):
		return self.name

	# def clean_description(self, *args, **kwargs):
	# 	print('h')
	# 	description = self.cleaned_data.get('description')
	# 	if len(description) < 10:
	# 		raise forms.ValidationError("Error to long")
	# 	else:
	# 		return description
