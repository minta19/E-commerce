from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()
class Product(models.Model):
    P_name=models.CharField(max_length=255,null=True)
    Price=models.FloatField()
    Quantity=models.IntegerField(default=0)
    image=models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self) -> str:
        return self.P_name
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.FloatField()
    ordered_at=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product.P_name} - {self.quantity}"
    
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.product.P_name} - {self.quantity}"
