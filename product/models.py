from django.db import models
from django.contrib.auth.models import User
#from cloudinary.models import CloudinaryField
from djangoproject import settings

class Product(models.Model):
    name = models.CharField(max_length=200, default="product")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    if settings.DEBUG:
         image = models.ImageField(upload_to='products/')
    else:     
        image =  image = CloudinaryField('image') 
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):  # Renamed from CartProduct to Cart
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True)
    products = models.ManyToManyField(Product, related_name='carts', blank=True)  

    def __str__(self):
        return f"{self.user.username}'s Cart"  

class Buying(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buy', null=True)
    products = models.ManyToManyField(Product, related_name='buy', blank=True)  

    def __str__(self):
        return f"{self.user.username}'s Buyings"  

class Wallet(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='wallet', null=True) 
    balance = models.IntegerField(default=1000)  

    def __str__(self):
        return f"{self.user.username}'s wallet"  
