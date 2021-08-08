from django import forms
from .models import Artist

from django.core.exceptions import ValidationError

from venues.forms import (name_validator, city_validator, 
                          url_validation, image_url_validation,
                          state_choice, genre_choice)

import re 

class ArtistModelForm(forms.ModelForm):
    name = forms.CharField(required=True, validators=[name_validator])
    city = forms.CharField(required=True, validators=[city_validator])
    state = forms.CharField(required=True, widget=forms.Select(choices=state_choice))
    address = forms.CharField(required=True)
    genre = forms.MultipleChoiceField(required=True, 
                widget=forms.SelectMultiple,
                choices=genre_choice)
    
    class Meta:
        model = Artist
        fields = [
            'name',
            'city',
            'state',
            'genre',
            'address',
            'phone',
            'facebook_link',
            'image_link',
            'website_link',
            "seeking_venue",
            'seeking_description'
        ]
    
    def clean_facebook_link(self):
        facebook_link = self.cleaned_data.get('facebook_link')
        if (facebook_link == None) or (facebook_link == ''):
            return facebook_link
        else:
            valid_url = url_validation(facebook_link)
            if valid_url:
                return facebook_link
            else:
                raise ValidationError('This is not a valid url') 

    def clean_website_link(self):
        website_link = self.cleaned_data.get('website_link')
        if (website_link == None) or (website_link == ''):
            return website_link
        else:
            valid_url = url_validation(website_link)
            if valid_url:
                return website_link
            else:
                raise ValidationError('This is not a valid url') 
         
    def clean_image_link(self):
        image_link = self.cleaned_data.get('image_link')
        if (image_link == None) or (image_link == ''):
            return image_link
        else:
            valid_image_url = image_url_validation(image_link)
            if valid_image_url:
                return image_link
            else:
                raise ValidationError('This is not a valid image url')