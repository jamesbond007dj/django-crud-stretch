from django.urls import path

from .views import MovieDetailView, MovieListView , MovieCreateView, MovieUpdateView , MovieDeleteView

urlpatterns = [
    path('mov/<int:pk>/', MovieDetailView.as_view(), name='mov_detail'),
    path('', MovieListView.as_view(), name='mov'),
    path('mov/new/', MovieCreateView.as_view(), name='mov_new'),
    path('mov/<int:pk>/edit/', MovieUpdateView.as_view(), name='mov_edit'),
    path('mov/<int:pk>/delete/', MovieDeleteView.as_view(), name='mov_delete'),
]