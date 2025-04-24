from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Selecciona un autor"
    )
    class Meta:
        model = Book
        exclude = ['editor']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título del libro'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción del libro'}),
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
