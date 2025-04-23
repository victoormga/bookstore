from django.shortcuts import render, get_object_or_404
from .models import Book
from django.core.paginator import Paginator

# Vista para listar libros
def book_list(request):
    books = Book.objects.all().order_by('-published_date')
    paginator = Paginator(books, 5)  # 5 libros por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {'page_obj': page_obj})


# Vista para ver detalle de un libro
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_details.html', {'book': book})
