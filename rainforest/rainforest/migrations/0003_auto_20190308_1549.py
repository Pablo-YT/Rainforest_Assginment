# Generated by Django 2.1.5 on 2019-03-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainforest', '0002_auto_20190308_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='priceincents',
            field=models.IntegerField(),
        ),
    ]