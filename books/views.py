from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Vista para listar libros
def book_list(request):
    books = Book.objects.all().order_by('-published_date')
    paginator = Paginator(books, 5)  # 5 libros por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {'page_obj': page_obj})


# Vista para ver detalle de un libro
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_details.html', {'book': book})

@login_required
def create_book(request):
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para añadir libros.')
        return redirect('book_list')
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.editor = request.user
            book.save()
            form.save_m2m()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    
    return render(request, 'books/create_book.html', {'form': form})