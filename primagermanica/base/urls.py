from django.urls import path, include

from primagermanica.base import views

urlpatterns = [
    path('<str:artist>/', views.ArtistView.as_view()),
]