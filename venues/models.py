from django.contrib.postgres.fields import ArrayField

from django.db import models
from django.urls import reverse

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    city = models.CharField(max_length=120, blank=False, null=False)
    state = models.CharField(max_length=120, blank=False, null=False)
    address = models.CharField(max_length=120, null=False, blank=False)
    phone = models.CharField(max_length=120, null=True, blank=True)
    image_link = models.URLField(max_length=500, blank=True, null=True)
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    genre =  ArrayField(models.CharField(max_length=50, blank=False, null=False))
    website_link = models.URLField(max_length=500, blank=True, null=True)
    seeking_talent = models.BooleanField(default=False)
    seeking_description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('venues:venue-detail', kwargs={"pk": self.id} )
