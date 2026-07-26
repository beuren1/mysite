from django.urls import path

from blog.views.post_view import post_view

urlpatterns = [
    path("", post_view, name="home"),
]
