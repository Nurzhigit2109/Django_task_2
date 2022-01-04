from django.shortcuts import render
from novelty.models import Books, Comments
from novelty.forms import CommentsForm
# Create your views here.

def novelty(request):
    book = Books.objects.order_by("-created")
    context = {
        "books": book
    }
    return render(request, "novelty.html", context=context)


def book_detail(request, id):
    book = Books.objects.get(id=id)
    if request.method == "GET":
        form = CommentsForm()
    elif request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            form.save()
    comment = Comments.objects.filter(book=book)
    context = {
        "books": book,
        "forms": form,
        "comments": comment
    }
    return render(request, "book_detail.html", context=context)