from django.urls import path, include

from .views import (ArtistListView, ArtistCreateView, 
                    ArtistDetailView, ArtistEditView,
                    ArtistDeleteView, ArtistSearchView)

app_name = "artists"

urlpatterns = [
    path('', ArtistListView.as_view(), name='artist-list'),
    path('search', ArtistSearchView.as_view(), name="artist-search"),
    path('create/', ArtistCreateView.as_view(), name='artist-create'),
    path('<int:pk>', ArtistDetailView.as_view(), name="artist-detail"),
    path('<int:pk>/edit', ArtistEditView.as_view(), name="artist-edit"),
    path('<int:pk>/delete', ArtistDeleteView.as_view(), name="artist-delete")
]