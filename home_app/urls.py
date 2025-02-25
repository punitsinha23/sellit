from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path('<str:username>/home', views.user_home ,name='userhome'),
    path('<str:username>/checkout/<int:pk>/', views.checkout_product, name='checkoutproduct'),
    path('buy/<int:pk>/<str:username>/', views.buying, name='buying_product'),  
]