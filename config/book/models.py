from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, verbose_name='آدرس')

    def __str__(self):
        return self.first_name    

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.first_name    

class Book(models.Model):
    title = models.CharField(max_length=70, verbose_name="نام کتاب")
    slug = models.SlugField(unique=True, verbose_name='آدرس')
    athore = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="نویسنده کتاب", related_name="book_athore")
    description = models.TextField(verbose_name="توضیحات کتاب")
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name="عکس محصول")
    release_date = models.DateField(verbose_name="تاریخ انتشار کتاب")
    reserve = models.BooleanField(default=False, verbose_name="رزرو شده ؟")
    genre = models.ManyToManyField(Genre, related_name='book_genre', verbose_name="ژانر کتاب")
    
    def __str__(self):
        return self.name