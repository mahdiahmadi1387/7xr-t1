from django.contrib import admin

from .models import Book, Topic, Ages, Author, Comment

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # نمونه فیلدهایی که در صفحه ادمین کتاب دیده شود
    # list_display = ('title', 'description', 'graph', 'svgid')
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Ages)
class AgesAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')