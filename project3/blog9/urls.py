from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('funk25/', views.funk25, name = 'funk25'),
    path('funk26/', views.funk26, name = 'funk26'),
    path('funk27/', views.funk27, name = 'funk27'),
]