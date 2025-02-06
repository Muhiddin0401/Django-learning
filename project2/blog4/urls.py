from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('funk10/', views.funk10, name = 'funk10'),
    path('funk11/', views.funk11, name = 'funk11'),
    path('funk12/', views.funk12, name = 'funk12'),
]