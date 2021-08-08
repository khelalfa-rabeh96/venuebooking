from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View

from datetime import datetime

from .models import Artist 
from .forms import ArtistModelForm
from venues.models import Venue
from shows.models import Show



class ArtistMixinObject(object):
    model = Artist 
    lookup = 'pk'

    def get_object(self):
        pk = self.kwargs.get(self.lookup)
        obj = None 
        if pk is not None:
            try:
                obj = Artist.objects.get(pk=pk)
            except Artist.DoesNotExist:
                pass

        return obj

# Create your views here.



class ArtistListView(View):
    template_name = "artists/artist_list.html"

    def get(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        
        # use this path in the search form to determine what we searching for
        path = request.path.translate({ord(c): None for c in '/'})
        context = {
            "artists": artists,
            "path": path
        }

        print (request.path_info)

        return render(request, 'artists/artist_list.html', context)

class ArtistSearchView(View):
    template_name = "artists/artist_search.html"

    def post(self, request, *args, **kwargs):
        search_term = request.POST['search_term']
        artists = Artist.objects.filter(name__icontains=search_term)

        for venue in artists:
            num_upcoming_shows = Show.objects.filter(venue = venue.id).count()
        context = {
            "search_term": search_term,
            "results": {
                "data": artists,
                "count": artists.count()
            }
            
        }
        return render(request, self.template_name, context)


class ArtistCreateView(View):
    template_name = "artists/artist_create.html"

    def get(self, request, *args, **kwargs):
        form = ArtistModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ArtistModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "An artist was created successfully.")
            return HttpResponseRedirect('/artists')
        else:
            messages.error(request, "Some data is not valid.")
            context = {"form": form}
            return render(request, self.template_name, context)


class ArtistDetailView(ArtistMixinObject, View):
    template_name = "artists/artist_detail.html"

    def get(self, request, *args, **kwargs):
        artist = self.get_object()

        if artist is not None:
            # Get all the shows that match this artist
            shows = Show.objects.filter(artist = artist.id)
        
            today = datetime.now()
            # Get the past and upcoming shows depend on today date
            past_shows = shows.exclude(start_time__gte = today)
            upcoming_shows = shows.filter(start_time__gte= today)

            # Count pas and upcoming shows
            past_shows_count = past_shows.count()
            upcoming_shows_count = upcoming_shows.count()

            # retrieve  the venue data and the start_time from the past shows
            past_shows_data = []
            if past_shows_count > 0:
                for past_show in past_shows:
                    venue = Venue.objects.get(pk=past_show.venue.id)
                    show_data = {
                        "venue_id": venue.id,
                        "venue_name": venue.name,
                        "venue_image_link": venue.image_link,
                        "start_time": past_show.start_time
                    }
                    past_shows_data.append(show_data)
            
            # retrieve  the venue data and the start_time from the upcoming shows
            upcoming_shows_data = []
            if upcoming_shows_count > 0:
                for upcoming_show in upcoming_shows:
                    venue = Venue.objects.get(pk=upcoming_show.venue.id)
                    show_data = {
                        "venue_id": venue.id,
                        "venue_name": venue.name,
                        "venue_image_link": venue.image_link,
                        "start_time": upcoming_show.start_time
                    }
                    upcoming_shows_data.append(show_data)
            

             
            context = {
                "artist": artist,
                "past_shows": past_shows_data,
                "upcoming_shows": upcoming_shows_data,
                "past_shows_count": past_shows_count,
                "upcoming_shows_count": upcoming_shows_count
                }

            return render(request, self.template_name, context)
        else:
            messages.warning(request, "This artist doesn't exists")
            return render(request, "errors/404.html")

class ArtistEditView(ArtistMixinObject, View):
    template_name = "artists/artist_edit.html"

    def get(self, request, *args, **kwargs):
        artist  = self.get_object()
        
        if artist is not  None :
            form = ArtistModelForm(instance=artist)
            context = {"form": form}
            return render(request, self.template_name, context)
        
        else:
            messages.warning(request, "This artist doesn't exists")
            return render(request, "errors/404.html")
    

    def post(self, request, *args, **kwargs):
        artist = self.get_object()
        if artist is not  None :
            form = ArtistModelForm(request.POST or None , instance=artist)
            
            if form.is_valid():
                form.save()
                messages.success(request, "This artist was updated successfully.")
                return HttpResponseRedirect(artist.get_absolute_url())
            else:
                context = {"form": form}
                messages.warning(request, "Some data is not valid")
                return render(request, self.template_name, context)
        
        else:
            messages.warning(request, "This artist doesn't exists")
            return render(request, "errors/404.html")

class ArtistDeleteView(ArtistMixinObject, View):
    
    def post(self, request, *args, **kwargs):
        artist = self.get_object()

        if artist is not None :
            artist.delete()
            messages.success(request, "The artist was deleted successfully.")
            return HttpResponseRedirect('../')
        else:
            messages.warning(request, "This artist doesn't exists")
            return HttpResponseRedirect(request, "errors/404.html")