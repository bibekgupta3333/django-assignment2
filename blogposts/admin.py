from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "status",
        "created",
        "updated",
        "count",
    )
    list_filter = (
        "author",
        "status",
        "created",
        "updated",
        "count",
    )
    search_fields = (
        "title",
        "body",
    )
    list_display_links = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "created_at",
    )
