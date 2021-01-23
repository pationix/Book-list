from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home(request):
    books = Book.objects.all()

    form = BookForm()
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"books":books, 'form':form}
    return render(request, "homepage.html", context)

def updateBook(request, pk):
    book = Book.objects.get(id=pk)

    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'update_book.html', context)

def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book':book}

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    return render(request, 'delete_book.html', context)

def previewBook(request, pk):
    book = Book.objects.get(id=pk)
    context = {'bookp':book}

    return render(request, 'preview_book.html', context)

def contactView(request):
    if request.method == 'GET':
        formC = ContactForm()
    else:
        formC = ContactForm(request.POST)
        if formC.is_valid():
            subject = formC.cleaned_data['subject']
            from_email = formC.cleaned_data['from_email']
            message = formC.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.123'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "email.html", {'formC': formC})
