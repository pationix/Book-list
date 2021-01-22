from .models import *
from .forms import *
from django.shortcuts import render, redirect

def home(request):
    books = Book.objects.all()
    print (Book.objects.all())

    form = BookForm()
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"books":books, 'form':form}
    return render(request, "homepage.html", context)