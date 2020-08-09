"""
This module provides custom profile  model.
"""
from django.db import models

# Create your models here.

from django.db import models
from authentication.models import UserProfile


class Orders(models.Model):
    """
    Attributes:
        OrderPlaced (str):User's orders,
        Goods(str):Describe what user's goods,
        birthday(date):User's birthday
    """
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="profile")
    order_placed = models.DateField()
    goods = models.CharField(max_length=50, blank=True)
