from django.contrib import admin

from blog.models import Post, Category, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "category", "is_published")
    prepopulated_fields = {"slug": ("title",), }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
