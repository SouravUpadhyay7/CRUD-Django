from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponse

# Create
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publication_date = request.POST['publication_date']
        Book.objects.create(title=title, author=author, publication_date=publication_date)
        return redirect('book_list')
    return render(request, 'books/create_book.html')

# Read
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# Update
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_date = request.POST['publication_date']
        book.save()
        return redirect('book_list')
    return render(request, 'books/update_book.html', {'book': book})

# Delete
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

