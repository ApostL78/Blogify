from import_export import resources

from blog.models import Post, Category, Comment


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
