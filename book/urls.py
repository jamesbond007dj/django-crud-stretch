from django.urls import path

from .views import BookDetailView, BookListView , BookCreateView, BookUpdateView , BookDeleteView

urlpatterns = [
    path('bk/<int:pk>/', BookDetailView.as_view(), name='bk_detail'),
    path('', BookListView.as_view(), name='bk'),
    path('bk/new/', BookCreateView.as_view(), name='bk_new'),
    path('bk/<int:pk>/edit/', BookUpdateView.as_view(), name='bk_edit'),
    path('bk/<int:pk>/delete/', BookDeleteView.as_view(), name='bk_delete'),
]