from django.contrib import admin
from .models import Book, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'slug', 'status', 'uploaded_on')
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'uploaded_on')
    summernote_fields = ('excerpt')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'book', 'uploaded_on', 'approved')
    list_filter = ('approved', 'uploaded_on')
    search_fields = ('name', 'email', 'body')
    
    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)