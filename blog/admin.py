from django.contrib import admin
from import_export.admin import ExportMixin

from blog.models import Post, Category, Comment
from blog.resources import PostResource, CommentResource, CategoryResource


# Register your models here.
@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("title", "created", "category", "is_published")
    prepopulated_fields = {"slug": ("title",), }
    resource_classes = [PostResource]


@admin.register(Category)
class CategoryAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("title",)
    resource_classes = [CategoryResource]


@admin.register(Comment)
class CommentAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = [CommentResource]
