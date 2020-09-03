from django.urls import path, include

from primagermanica.base import views

urlpatterns = [
    path('', views.ArtistView.as_view()),
]