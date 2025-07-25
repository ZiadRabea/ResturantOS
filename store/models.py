from django.db import models
from Accounts.models import *
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.
class Store(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to="logos", storage=MediaCloudinaryStorage)
    banner = models.ImageField(upload_to="banners", storage=MediaCloudinaryStorage)
    app = models.CharField(max_length=1000)
    number = models.CharField(max_length=20)
    custom_order_link = models.CharField(max_length=1000, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name} | {self.owner}"

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="product images", storage=MediaCloudinaryStorage)
    currencies = (("egp", "egp"), ("usd", "usd"), ("eur", "eur"))
    currency = models.CharField(choices=currencies)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.CASCADE)
    savers = models.ManyToManyField(Profile, related_name="product_savers", null=True, blank=True)
    is_available = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        ordering=["-date"]
        
    def __str__(self):
        return f"{self.title}"


class StoreRequest(models.Model):
    store_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    notes = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submitted_at} | {self.store_name}"

class Category(models.Model):
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Categories", null=True, blank=True, storage=MediaCloudinaryStorage)

    def __str__(self):
        return f"{self.name} | {self.store.name}" 