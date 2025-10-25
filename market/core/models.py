from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


        