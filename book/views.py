from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy

from .models import Bk


class BookListView(ListView):
    model = Bk
    template_name = 'bk.html'


class BookDetailView(DetailView):
    model = Bk
    template_name = 'bk_detail.html'

class BookCreateView(CreateView):
    model = Bk
    template_name = 'bk_new.html'
    fields = ['title', 'author','genre', 'field_name','description']

class BookUpdateView(UpdateView):
    model = Bk
    template_name = 'bk_edit.html'
    fields = ['title', 'author','genre', 'field_name','description']

class BookDeleteView(DeleteView):
    model = Bk
    template_name = 'bk_delete.html'
    success_url = reverse_lazy('bk')
    