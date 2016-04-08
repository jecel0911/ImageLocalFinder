from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^dashboard', views.image_finder_index, name="image_finder_index"),
]