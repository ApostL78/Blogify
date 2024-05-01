from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from blog.filters import PostFilter
from blog.forms import CategoryForm, PostForm, RegistrationForm, CommentForm
from blog.models import Post, Category


class PostView(ListView):
    template_name = "blog/index.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["active_category"] = "all"
        context["filter"] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/update_post.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise PermissionDenied
        return super(UpdatePostView, self).post(request, *args, **kwargs)


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy("home")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["comments"] = context.get("post").comments.filter(active=True).order_by("-created")
        context["form"] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.active = True
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        return self.get(request)


class CategoryView(DetailView):
    model = Category
    template_name = "blog/category.html"
    context_object_name = "category"


class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog/add_category.html"


class PostsByCategoryView(DetailView):
    model = Category
    template_name = "blog/by_category.html"
    context_object_name = "category"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsByCategoryView, self).get_context_data(**kwargs)
        context["active_category"] = context.get("category").id
        context["post_list"] = Post.objects.filter(
            category=context.get("category"), is_published=True
        )
        return context


class RegisterUser(CreateView):
    """Register user by custom form"""

    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("home")
