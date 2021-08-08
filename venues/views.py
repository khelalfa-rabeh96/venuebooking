from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import View

from datetime import datetime

from .models import Venue 
from .forms import VenueModelForm
from shows.models import Show
from artists.models import Artist

# Create your views here.
def index(request):
    return render(request,'home.html')


class VenueMixinObject(object):

    model = Venue 
    lookup = 'pk'

    def get_object(self):
        pk = self.kwargs.get(self.lookup)
        obj = None 
        if pk is not None:
            try:
                obj = Venue.objects.get(pk=pk)
            except Venue.DoesNotExist:
                pass

        return obj


class VenueListView(View):

    def get(self, request, *args, **kwargs):        
        # get all the cities and its state with no duplication 
        venue_area = Venue.objects.order_by('city', 'state').distinct(
        'city', 'state'
        )
        
        areas = []

        # Loop throught each area to add all the venues that are in this area
        for area in venue_area:
            city = area.city
            state = area.state

            # Get all the venues that belong to this area
            venues = Venue.objects.filter(city=city, state=state)
            
            area_data = {"city": city, "state": state, "venues": venues}
            areas.append(area_data)
        
        # use this path in the search form to determine what we searching for
        path = request.path.translate({ord(c): None for c in '/'})
        context = {
            "areas": areas,
            "path": path
        }

        return render(request, 'venues/venue_list.html', context)
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Post Method in this Endpoint is Not Allowed')

class VenueSearchView(View):
    template_name = "venues/venue_search.html"

    def post(self, request, *args, **kwargs):
        search_term = request.POST['search_term']
        venues = Venue.objects.filter(name__icontains=search_term)

        for venue in venues:
            num_upcoming_shows = Show.objects.filter(venue = venue.id).count()
        context = {
            "search_term": search_term,
            "results": {
                "data": venues,
                "count": venues.count()
            }
            
        }
        return render(request, self.template_name, context)

class VenueCreateView(View):
    template_name = "venues/venue_create.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VenueCreateView, self).dispatch(request, *args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        form = VenueModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = VenueModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "A venue was created successfully.")
            return HttpResponseRedirect('/venues')
        else:
            messages.error(request, "Seome data is not valid.")
            context = {"form": form}
            return render(request, self.template_name, context)



class VenueDetailView(VenueMixinObject, View):
    template_name = "venues/venue_detail.html"


    def get(self, request, *rags, **kargs):
        venue = self.get_object()

        if venue is not None :
            # Get all the shows that match this venue
            shows = Show.objects.filter(venue = venue.id)
        
            today = datetime.now()
            # Get the past and upcoming shows depend on today date
            past_shows = shows.exclude(start_time__gte = today)
            upcoming_shows = shows.filter(start_time__gte= today)

            # Count pas and upcoming shows
            past_shows_count = past_shows.count()
            upcoming_shows_count = upcoming_shows.count()

            # retrieve  the artist data and the start_time from the past shows
            past_shows_data = []
            if past_shows_count > 0:
                for past_show in past_shows:
                    artist = Artist.objects.get(pk=past_show.artist.id)
                    show_data = {
                        "artist_id": artist.id,
                        "artist_name": artist.name,
                        "artist_image_link": artist.image_link,
                        "start_time": past_show.start_time
                    }
                    past_shows_data.append(show_data)
            
            # retrieve  the venue data and the start_time from the upcoming shows
            upcoming_shows_data = []
            if upcoming_shows_count > 0:
                for upcoming_show in upcoming_shows:
                    artist = Artist.objects.get(pk=upcoming_show.artist.id)
                    show_data = {
                        "artist_id": artist.id,
                        "artist_name": artist.name,
                        "artist_image_link": artist.image_link,
                        "start_time": upcoming_show.start_time
                    }
                    upcoming_shows_data.append(show_data)
            

             

            context = {
                "venue": venue,
                "past_shows": past_shows_data,
                "upcoming_shows": upcoming_shows_data,
                "past_shows_count": past_shows_count,
                "upcoming_shows_count": upcoming_shows_count
                }
            return render(request, self.template_name, context)
        else: 
            messages.error(request, "This venue Doesn't exist")
            return render(request, "errors/404.html")


class VenueEditView(VenueMixinObject, View):
    template_name = "venues/venue_edit.html"
    
    def get(self, request, *args, **kwargs):
        venue = self.get_object()
        if venue is not None :
            form = VenueModelForm(instance=venue)
            context = {"form": form}
            return render(request, self.template_name, context)
        else: 
            messages.error(request, "This venue Doesn't exist")
            return render(request, "errors/404.html")


    def post(self, request, *args, **kwargs):
        venue = self.get_object()
        if venue is not None :
            form = VenueModelForm(request.POST or None, instance=venue)
            context = {"form": form}
            if form.is_valid():
                form.save()
                messages.success(request, "This venue was updated successfully.")
                return HttpResponseRedirect(venue.get_absolute_url())
            
            else: 
                messages.warning(request, "Some data is not valid")
                return render(request, self.template_name, context)

       
        else :
            messages.warning(request, "This venue Doesn't exist")
            return render(request, "errors/404.html")


class VenueDeleteView(VenueMixinObject, View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Get Method in this Endpoint is Not Allowed')

    def post(self, request, *rags, **kargs):
        venue = self.get_object()
        if venue is not None :
            venue.delete()
            messages.success(request, "This venue was deleted successfully.")
            return HttpResponseRedirect('../')
        else: 
            messages.error(request, "This venue Doesn't exist")
            return render(request, "errors/404.html")

