from django.urls import path
from .views import *

app_name = 'films'
urlpatterns = [
    path('', FilmListView.as_view(), name='all'),
    path('films/<int:pk>/detail', FilmDetailView.as_view(), name="film_detail"),
    path('films/create', FilmCreateView.as_view(), name='film_create'),
    path('films/<int:pk>/update', FilmUpdateView.as_view(), name='film_update'),
    path('film/<int:pk>/delete',FilmDeleteView.as_view(), name='film_delete'),
    
]