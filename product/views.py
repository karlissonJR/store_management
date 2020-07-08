from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product:list_products')

@login_required
def create_product(request):
    form = ProductForm(request.POST or None)
    print('ERROS: %s' % form.errors)

    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()

        return redirect('product:list_products')

    return render(request, 'product/products_form.html', {'form': form})

@login_required
def list_products(request):
    products = Product.objects.filter(user=request.user)
    
    return render(request, 'product/list_products.html', {'products': products})

@login_required
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product:list_products')

    return render(request, 'product/products_form.html', {
        'product': product,
        'form': form,
    })