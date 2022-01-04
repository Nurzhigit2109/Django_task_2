from django.urls import path, include
from .views import novelty, book_detail

urlpatterns = [
    path('', novelty , name="novelty"),
    path('book_detail/<int:id>', book_detail, name="book_detail"),
]