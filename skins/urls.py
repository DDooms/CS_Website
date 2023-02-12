from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('skins/', views.index, name='skins'),
    path('gmail/', views.gmail, name='gmail'),
    path('send/', views.send, name='send'),
]


