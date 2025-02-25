from django.contrib import admin
from .models import Product , Cart , Buying , Wallet

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Buying)
admin.site.register(Wallet)
