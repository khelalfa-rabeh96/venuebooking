from django import forms
from .models import Venue 
from django.core.validators import URLValidator
import re
from django.core.exceptions import ValidationError

state_choice = [
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
genre_choice = [
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]


def check_regx(reg_exp, text):
    if re.search(reg_exp, text):
        return text 
    else:
        return False



def name_validator(text):
    reg_exp = "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
    if check_regx(reg_exp, text):
        return text 
    else:
        raise ValidationError("This is not a valid name")

def city_validator(text):
    reg_exp = "^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$"
    if check_regx(reg_exp, text):
        return text 
    else: 
        raise ValidationError("This is not a valid city name")


def url_validation(url):
    validator = URLValidator()

    try:
        validator(url)
        return True 
    except ValidationError as exception:
        return False

def image_url_validation(image_url):
    reg_exp = "(https?:\/\/.*\.(?:png|jpg|gif))"
    return check_regx(reg_exp, image_url)
    

class VenueModelForm(forms.ModelForm):
    name = forms.CharField(required=True, validators=[name_validator])
    city = forms.CharField(required=True, validators=[city_validator])
    state = forms.CharField(required=True, widget=forms.Select(choices=state_choice))
    address = forms.CharField(required=True)
    genre = forms.MultipleChoiceField(required=True, 
                widget=forms.SelectMultiple,
                choices=genre_choice
            )

    class Meta: 
        model = Venue
        fields = [
            'name',
            'city',
            'state',
            'address',
            'phone',
            'image_link',
            'facebook_link',
            'genre',
            'website_link',
            "seeking_talent",
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
    

    