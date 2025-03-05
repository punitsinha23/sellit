from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:username>/', views.create_product, name='create'),
    path('list/<str:username>/', views.product_list, name='product_list'),
    path('cart/<str:username>/<int:pk>/', views.cart_product, name='cart_product'),
    path('view-cart/<str:username>/', views.view_cart, name='view_cart'),
    path('update/<int:pk>/<str:username>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/<str:username>/', views.delete_product, name='delete_product'),
    path('detail/<int:pk>/<str:username>/', views.detail_product, name='detail_product'),
    path('search/', views.search_user, name='search'),
    path('profile/<str:username>/', views.user_profile, name='users_profile'), 
]
