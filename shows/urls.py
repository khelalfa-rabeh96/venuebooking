from django.urls import path 
from .views import (ShowCreateView, ShowListView)

app_name = "shows"

urlpatterns = [
    path('', ShowListView.as_view(), name="show-list"),
    path('create/', ShowCreateView.as_view(), name="show-create")
]