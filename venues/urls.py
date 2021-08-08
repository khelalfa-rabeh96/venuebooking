from django.urls import path, include

from .views import (VenueListView, 
                    VenueCreateView,
                    VenueEditView,
                    VenueDetailView,
                    VenueDeleteView,
                    VenueSearchView)

app_name = "venues"

urlpatterns = [
    path('', VenueListView.as_view(), name="venue-list"),
    path('search', VenueSearchView.as_view(), name="venue-search"),
    path('create/', VenueCreateView.as_view(), name="venue-create"),
    path('<int:pk>/', VenueDetailView.as_view(), name="venue-detail"),
    path('<int:pk>/edit', VenueEditView.as_view(), name="venue-edit"),
    path('<int:pk>/delete',VenueDeleteView.as_view(), name="venue-delete"),
]