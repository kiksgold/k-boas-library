from django.shortcuts import render
from django.views import generic
from .models import Book


class BookList(generic.BookView):
    model = Book
    queryset = Book.objects.filter(status=1).order_by('-updated_on')
    template_name = 'index.html'
    paginate_by = 4
