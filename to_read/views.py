from django.shortcuts import render
from novelty.models import Books, Comments
from novelty.forms import CommentsForm
from django.db.models import Count

# Create your views here.

def to_read(request):
    book = Books.objects.order_by('?').first()
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
        'book': book,
        "forms": form,
        "comments": comment
    }
    return render(request, "to_read.html", context=context)

