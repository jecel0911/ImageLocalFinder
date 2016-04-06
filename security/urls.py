from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^security/profile', views.profile, name="security"),
]