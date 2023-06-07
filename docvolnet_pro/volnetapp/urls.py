from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:id>/update/', views.product_update, name='product_update'),
    path('product/<int:id>/delete/', views.product_delete, name='product_delete'),
]
