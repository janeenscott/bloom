from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# What it means to be a rental-- information describing the listed item
class Rental(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    item = models.CharField(max_length=255)
    price = models.IntegerField(default=1923)
    image = models.URLField()
