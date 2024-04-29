from django.urls import path 
from . import views 


urlpatterns = [
    path('register/', views.registerUsers, name="register"),
    path('login/', views.login, name="login"),
    path('logout', views.user_logout, name="logout"),
]


app_name = "users"