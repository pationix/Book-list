from django.urls import path

from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('update_book/<str:pk>/', views.updateBook, name="update_book")
]