from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('create/', views.product_create, name='product-create'),
    path('update/<int:pk>/', views.product_update, name='product-update'),
    path('delete/<int:pk>/', views.product_delete, name='product-delete'),
]
