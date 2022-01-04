from django.shortcuts import render
from novelty.models import Books
# Create your views here.
def home(request):
    books = Books.objects.all()
    context = {
        "books": books
    }
    return render(request, "home.html", context=context)