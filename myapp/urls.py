from django.urls import path

from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('update_book/<str:pk>/', views.updateBook, name="update_book"),
    path('delete_book/<str:pk>/', views.deleteBook, name="delete_book"),
    path('preview_book/<str:pk>/', views.previewBook, name="preview_book"),
    path('contact/', views.contactView, name='contact'),
]