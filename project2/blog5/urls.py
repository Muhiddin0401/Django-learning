from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('funk13/', views.funk13, name = 'funk13'),
    path('funk14/', views.funk14, name = 'funk14'),
    path('funk15/', views.funk15, name = 'funk15'),
]