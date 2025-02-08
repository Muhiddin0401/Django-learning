from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('funk22/', views.funk22, name = 'funk22'),
    path('funk23/', views.funk23, name = 'funk23'),
    path('funk24/', views.funk24, name = 'funk24'),
]