from django.contrib import admin

# Register your models here.
from .models import book_item

admin.site.register(book_item)