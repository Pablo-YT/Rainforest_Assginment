"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rainforest.views import products, products_show, root, product_create, product_edit, product_delete, product_review, edit_review, delete_review
from rainforest.forms import product_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name='products_home'),
    path('products/<int:id>',products_show, name='products_show'),
    path('create/', product_create, name='product_create'),
    path('products/<int:id>/edit', product_edit, name='product_edit'),
    path('products/<int:id>/delete', product_delete, name='product_delete'),
    path('products/<int:id>/review', product_review, name='product_review'), #DONT NEED THIS LINE BUT DONT KNOW HOW TO DELTE
    path('review/<int:id>', edit_review, name='edit_review'),
    path('review/<int:id>/delete', delete_review, name='delete_review'),
    path('', root)

]
