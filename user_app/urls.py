from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.user_dashboard, name='profile'),
    path('cart/<str:username>/', views.user_dashboard, name='cart'),
    path('buying/<str:username>/', views.buying_list , name='buying_list'),

]
