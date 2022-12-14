from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie

class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft = False)
    template_name = "movies/movies.html"

class MovieDetailView(DetailView):
    """Описание фильма"""
    model = Movie
    slug_field = "url"
