from django.http import HttpResponse
from .models import Book
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book' :book})

