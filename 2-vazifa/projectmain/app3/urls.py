from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path("func7/", views.func7, name = "func7"),
    path("func8/", views.func8, name = "func8"),
    path("func9/", views.func9, name = "func9"),
]