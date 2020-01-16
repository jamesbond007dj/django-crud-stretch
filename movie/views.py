from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy

from .models import Mov


class MovieListView(ListView):
    model = Mov
    template_name = 'mov.html'


class MovieDetailView(DetailView):
    model = Mov
    template_name = 'mov_detail.html'

class MovieCreateView(CreateView):
    model = Mov
    template_name = 'mov_new.html'
    fields = ['title', 'genre','director', 'starring', 'field_name','description']

class MovieUpdateView(UpdateView):
    model = Mov
    template_name = 'mov_edit.html'
    fields = ['title', 'genre','director', 'starring', 'field_name','description']

class MovieDeleteView(DeleteView):
    model = Mov
    template_name = 'mov_delete.html'
    success_url = reverse_lazy('mov')
    