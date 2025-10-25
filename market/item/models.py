from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) #It's a foreign key field, which means it will establish a link between Item and Category models. An item will be associated with a category."related_name='items'":It means that we can access all items associated with a category using category.items.all(). 'on_delete=models.CASCADE': which means that when a Category is deleted, all associated Item records will also be deleted.
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True) #Django will created the uploaded folder for us if it doesn't exist. In case the user doesn't want to provide an image so black = True and null = True 
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    