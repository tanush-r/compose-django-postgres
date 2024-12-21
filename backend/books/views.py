from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def get_all(request):

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    form = BookForm()
    print(form)
    books = list(Book.objects.values())
    return render(request, 'books.html', {'data':books, 'form': form})

