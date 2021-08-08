from django.shortcuts import render, redirect
from django.views import View
from django.http import  HttpResponseRedirect
from django.contrib import messages

from .models import Show
from .forms import ShowModelForm
from venues.models import Venue 
from artists.models import Artist

# Create your views here.

class ShowListView(View):

    template_name = "shows/show_list.html"

    def get(self, request, *args, **kwargs):
        query_list = Show.objects.all() 
        shows = []
        for query in query_list:
            venue = Venue.objects.get(pk=query.venue.id)
            artist = Artist.objects.get(pk=query.artist.id)
            show = {
                "venue_id" : venue.id,
                "venue_name": venue.name,
                "artist_id" : artist.id,
                "artist_name": artist.name,
                "artist_image_link": artist.image_link ,
                "start_time": query.start_time
                
            }

            shows.append(show)

        # use this path in the search form to determine what we searching for
        path = request.path.translate({ord(c): None for c in '/'})

        context = {
            "shows": shows,
            "path": path
            }
        return render(request, self.template_name, context)

class ShowCreateView(View):
    template_name = "shows/show_create.html"

    def get(self, request, *args, **kwargs):
        form = ShowModelForm()
        context = {'form': form}            
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ShowModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.warning(request, 'A show was created succesfully')
            return HttpResponseRedirect('/venues')
        else:
            messages.warning(request, 'Some data is not valid')
            context = {'form': form}            
            return render(request, self.template_name, context)
            
        