from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH




class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True),
    nome = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True,blank=True,default="/images/placeholder.png", upload_to='images/'),
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True),
    description = models.TextField(null=False,blank=True),
    rating = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    numReviews = models.ImageField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self) -> str:
        return self.name + " | " + self.brand+ " | " + str(self.price)