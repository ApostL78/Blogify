import django_filters
from django.forms import fields
from django_filters import CharFilter
from blog.models import Post


class BootstrapStylesFiltersMixin:
    filters = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.filters:
            for fieldname in self.filters:
                class_object = self.filters[fieldname]
                if hasattr(self.filters[fieldname].field, "empty_label"):
                    self.filters[fieldname].field.empty_label = "выбрать..."
                    self.filters[fieldname].field.widget.attrs["class"] = "form-select"
                    continue
                if isinstance(class_object, fields.BooleanField):
                    continue
                self.filters[fieldname].field.widget.attrs["class"] = "form-control"


class PostFilter(BootstrapStylesFiltersMixin, django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains",
                       label="заголовок")
    content = CharFilter(field_name="content", lookup_expr="icontains",
                       label="описание")

    class Meta:
        model = Post
        fields = ("title", "content")
