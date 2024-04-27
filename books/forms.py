from django import forms
from .models import Book, Category


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50) 
    

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=20, 
        min_length=3, 
        required=True,
    )
    class Meta:
        model = Category
        fields = ['name']


class BooksForm(forms.ModelForm):
    title = forms.CharField(max_length=50, min_length=10, required=True)
    author = forms.CharField(max_length=50, min_length=10, required=True)
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'category']
    