from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Ajout d'un related_name personnalisé
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Ajout d'un related_name personnalisé
        blank=True
    )

    # Ajoutez d'autres champs nécessaires pour votre utilisateur personnalisé

    def __str__(self):
        return self.username

'''
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('client','Client'),
        ('vendeur','Vendeur'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    
    def __str__(self):
        return f"{self.username} ({self.role})"

'''

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Ajoutez d'autres champs nécessaires pour le produit

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    #comlpeter d'autres champs pour les commandes

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    #comlpeter d'autres champs pour les commandes

    def __str__(self):
        return f"Cart of {self.user.username}"


