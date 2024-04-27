from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200,unique=True, null=False, blank=False)
    author = models.CharField(max_length=200,null=False, blank=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title