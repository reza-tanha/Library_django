from django.contrib import admin
from .models import Book, Author, Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',"slug")
    list_filter = ('title', )
    prepopulated_fields = {'slug':('title',)}



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',"slug","athore","release_date","reserve")
    list_display_links = ('title',"athore")
    list_filter = ('title', 'athore', 'release_date', 'reserve', 'genre')
    list_editable = ('slug', 'reserve',)
    prepopulated_fields = {'slug':('title',)}

