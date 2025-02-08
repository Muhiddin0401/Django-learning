from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .import views

urlpatterns = [
    path('funk4/',views.funk4, name = "funk4"),
    path('funk5/',views.funk5, name = "funk5"),
    path('funk6/',views.funk6, name = "funk6"),
]