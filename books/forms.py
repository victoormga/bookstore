from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    author = forms.CharField(label='Autor', widget=forms.TextInput(attrs={'placeholder': 'Nombre del autor'}))

    class Meta:
        model = Book
        exclude = ['editor']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título del libro'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción del libro'}),
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
