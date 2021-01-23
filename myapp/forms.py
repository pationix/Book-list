from django import forms
from django.forms import ModelForm


from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
