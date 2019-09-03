
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('',views.register,name='register'),
    path('display/', views.display,name='display')
]
