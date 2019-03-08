from django.db import models
from django.core.exceptions import ValidationError

def validate_even(value):
    if len(value) > 10:
        raise ValidationError(
            print('error')
        )



class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(validators=[validate_even])
	price = models.CharField(max_length=255)


	def __str__(self):
		return self.name
