from django.urls import path

from url_shortener.views import index

urlpatterns = [
    path("", index, name="index"),
]
