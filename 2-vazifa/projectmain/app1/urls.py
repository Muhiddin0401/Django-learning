from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path("func1/", views.func1, name = "func1"),
    path("func2/", views.func2, name = "func2"),
    path("func3/", views.func3, name = "func3"),
]