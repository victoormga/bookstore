from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AuthorForm

@login_required
def add_author(request):
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para añadir autores.')
        return redirect('book_list')  # Puedes cambiar esto por donde quieras redirigir

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save() 
            messages.success(request, f'Se añadió el autor "{author.name}" correctamente.')
            return redirect('author_list')  
    else:
        form = AuthorForm()

    return render(request, 'authors/add_author.html', {'form': form})
