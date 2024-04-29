from django.shortcuts import render, redirect
from .models import Book, Category, BookImage
from .forms import BooksForm, CategoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required

@login_required(login_url='users:login')
def index(request):
    
    books = Book.objects.all()
    return render(
        request,
        'books/index.html',
        {"books":books}
    )
@login_required(login_url='users:login')
def details(request, id):
    book = Book.objects.get(id=id)
    return render(
        request,
        'books/details.html',
        {"book":book}
    )
    
@login_required(login_url='users:login')
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:index')
        else: 
            form = CategoryForm()
            messa = messages.error(request, form.errors)
            return render(
                request,
                'books/create_category.html',
                {"form":form, 'messa':messa}
            )
    else:
        form = CategoryForm()
        return render(
            request,
            'books/create_category.html',
            {"form":form}
        )
@login_required(login_url='users:login')  
def create_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:index')
        else: 
            form = BooksForm(instance=request.POST)
            messa = messages.error(request, form.errors)
            return render(
                request,
                'books/create_book.html',
                {"form":form, 'messa':messa}
            )
    else:
        form = BooksForm()
        return render(
            request,
            'books/create_book.html',
            {"form":form}
        )
        
        
@login_required(login_url='users:login')      
def uploadImage(request):
    if request.method == 'POST':
        if request.FILES:
            image = request.FILES['image']
            name = request.POST['name']
            BookImage.objects.create(name=name, image=image)
        return redirect('book:index')

    else:
        return render(
            request,
            'books/upload.html'
        )