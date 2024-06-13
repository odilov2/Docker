from django.shortcuts import render, redirect
from .models import Product
from django.views import View


class ProductView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'products.html', {'products': product})

