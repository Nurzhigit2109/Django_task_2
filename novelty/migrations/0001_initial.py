# Generated by Django 3.2.9 on 2021-12-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('book', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='books/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
