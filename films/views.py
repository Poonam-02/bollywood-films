from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .models import Film
import pdb

class FilmBaseView(View):
    model = Film
    fields = '__all__'
    succuss_url = reverse_lazy('films:all')
    

class FilmListView(FilmBaseView, ListView):
    model = Film
    template_name="films/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["film_list"] = Film.objects.all()
        return context
    


class FilmDetailView(FilmBaseView, DetailView):
    model = Film
    template_name="films/detail.html"
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    
class FilmCreateView(FilmBaseView, CreateView):
    model = Film
    template_name="films/create.html"
    success_url = reverse_lazy('films:all')


class FilmUpdateView(FilmBaseView, UpdateView):
    model = Film
    template_name="films/update.html"
    success_url = reverse_lazy('films:all')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["film"] = Film.objects
        return context
    
class FilmDeleteView(FilmBaseView, DeleteView):
    model = Film
    template_name="films/delete.html"
    success_url = reverse_lazy('films:all')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["film"] = Film.objects
        return context