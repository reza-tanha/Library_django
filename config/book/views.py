from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book


class Home(ListView):
    """
        List of all books available on the website.
    """
    template_name = 'book/books.html'
    context_object_name = 'books'
    ordering =['-title']
    model = Book


def book_detail(request, pk:int):
    """
        Display of a special book with ID
    """
    book = get_object_or_404(Book,pk=pk)
    context = {
        'book':book
    }
    return render(request, 'book/book-detail.html', context)

