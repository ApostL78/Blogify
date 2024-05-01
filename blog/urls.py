from django.urls import path

from blog.views import (
    PostView,
    CategoryView,
    PostsByCategoryView,
    CreateCategoryView,
    CreatePostView,
    RegisterUser,
    PostDetailView,
    UpdatePostView,
    DeletePostView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", PostView.as_view(), name="home"),
    path("by_category/<int:pk>/", PostsByCategoryView.as_view(), name="by_category"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
    path("add_category/", CreateCategoryView.as_view(), name="add_category"),
    path("add_post/", CreatePostView.as_view(), name="add_post"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post_update/<int:pk>/", UpdatePostView.as_view(), name="post_update"),
    path("post_delete/<int:pk>/", DeletePostView.as_view(), name="post_delete"),
]

urlpatterns += [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
