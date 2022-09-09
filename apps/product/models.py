from django.db import models

# Create your models here.
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='category', null=True, blank=True)
    serial = models.IntegerField(unique=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    