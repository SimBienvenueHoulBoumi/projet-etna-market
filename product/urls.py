from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.get_products),
    path('create/', views.post_products),
    path('get/<int:product_id>/', views.get_product),
    path('update/<int:product_id>/', views.put_product),
    path('delete/<int:product_id>/', views.delete_product),
]