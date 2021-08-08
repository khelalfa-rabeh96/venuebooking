from django import forms

from .models import Show 
from venues.models import Venue
from artists.models import Artist



class ShowModelForm(forms.ModelForm):
    venue = forms.ModelChoiceField(queryset=Venue.objects.all())
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    start_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
       
    )

    class Meta:
        model = Show 
        fields = [
            'venue',
            'artist',
            'start_time'
        ]

