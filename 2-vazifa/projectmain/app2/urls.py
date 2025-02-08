from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path("func4/", views.func4, name = "func4"),
    path("func5/", views.func5, name = "func5"),
    path("func6/", views.func6, name = "func6"),
]