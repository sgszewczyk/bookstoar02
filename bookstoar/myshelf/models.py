from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class book_item(models.Model):
    book_title =        models.CharField(max_length=100)
    book_author =       models.CharField(max_length=100)
    book_description =  models.TextField(max_length=1000)
    book_price =        models.DecimalField(max_digits=6,decimal_places=2)
    book_year =         models.DecimalField(max_digits=4,decimal_places=0)
    book_review =       models.TextField(max_length=1000)
    book_acquired =     models.BooleanField(default=None)
    book_read =         models.BooleanField(default=None)