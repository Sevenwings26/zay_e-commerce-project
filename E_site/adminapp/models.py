from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# create models
class Profile(models.Model):
    position = [
        ("HR", "HR"),
        ("Accountant", "Accountant"),
        ("Manager", "Manager"),
        ("Customer care", "Customer care")
    ]
    
    state = [
        ("Oyo", "Oyo"),
        ("Lagos", "Lagos"),
        ("Imo", "Imo"),
    ]
    
    marital_status = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Complicated", "Complicated"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) # PROTECT
    position = models.CharField(choices=position, unique=False, max_length=20)
    state = models.CharField(choices=state, unique=False, max_length=20)
    marital_status = models.CharField(choices=marital_status, unique=False, max_length=20, default="DEFAULT VALUE")
    phone = models.CharField(unique=True, max_length=11, blank=True, null=True)

def __str__(self):
    return str(self.user)


# Table for product uploading 
class productCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    
# product table 
class productTable(models.Model):
    category = [
        ('Electronics', 'Electronics'),
        ('Wears', 'Wears'),
        ('Lotions', 'Lotions'),
        ('Gym-kit', 'Gym-kit'),
    ]
    
    productId = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to='product_image/', unique=True, null=True, blank=True)
    category = models.CharField(choices=category, unique=False, max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default = timezone.now)
    # created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, null=False, blank=False , on_delete=models.CASCADE)