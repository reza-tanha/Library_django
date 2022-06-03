from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book


class Home(ListView):
    template_name = 'book/books.html'
    context_object_name = 'books'
    ordering =['-title']
    def get_queryset(self):
        return Book.objects.all()


def book_detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    context = {
        'book':book
    }
    return render(request, 'book/book-detail.html', context)

