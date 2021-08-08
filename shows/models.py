from django.db import models
from venues.models import Venue
from artists.models import Artist
from django.utils import timezone
from datetime import datetime


# Create your models here.
class Show(models.Model):
    venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    start_time = models.DateTimeField(default= datetime.now, blank=True)