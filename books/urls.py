from .views import * 
from django.urls import path 


urlpatterns = [
    path('', index, name="index"),
    path('create_category/', create_category, name="create_category"),
    path('create_book/', create_book, name="create_book"),
    path('<int:id>/', details, name="details")
]


app_name = "book"