from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('funk19/', views.funk19, name = 'funk19'),
    path('funk20/', views.funk20, name = 'funk20'),
    path('funk21/', views.funk21, name = 'funk21'),
]