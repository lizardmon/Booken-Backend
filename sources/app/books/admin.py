from django.contrib import admin

from books.models import Book, BookReview


class BookReviewInlineAdmin(admin.StackedInline):
    model = BookReview


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookReviewInlineAdmin]
