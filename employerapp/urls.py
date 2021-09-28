from django.urls import path
from .views import *

urlpatterns = [
    path('anp', anp),
    path('showanp', showAnp),
    path('', showAnp),
    path('deleteAnp/<str:pk>/', deleteAnp),
    path('editAnp/<str:pk>/', editAnp), 
    path('updateAnp/<str:pk>/', updateAnp), 
]
