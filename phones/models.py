from django.db import models
from django.http import request
from django.utils.text import slugify

class Phone(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Phone, self).save(*args, **kwargs)