from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("", max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Категoрия",
    )
    photo = models.ImageField("Фото", upload_to="posts/%Y/%m/%d/", default="No photo")
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": str(self.pk)})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class Category(models.Model):
    title = models.CharField("Название категории", max_length=150, db_index=True)
    photo = models.ImageField(
        "Фото", upload_to="categories/%Y/%m/%d/", default="No photo"
    )
    about = models.CharField("О категории", max_length=200, null=True, blank=True)

    def post_count(self):
        return Post.objects.filter(category=self).count()

    def get_absolute_url(self):
        return reverse_lazy("category", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
