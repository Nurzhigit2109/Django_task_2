from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    book = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="books/")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Comments(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Имя")
    comment = models.TextField(verbose_name="Комментарий")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.name