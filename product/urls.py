from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'product'
urlpatterns = [
    path('', views.list_products, name='list_products'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', login_required(views.DeleteProduct.as_view()), name='delete_product'),
]