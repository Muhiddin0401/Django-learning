from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('funk7/', views.funk7, name = 'funk7'),
    path('funk8/', views.funk8, name = 'funk8'),
    path('funk9/', views.funk9, name = 'funk9'),
]