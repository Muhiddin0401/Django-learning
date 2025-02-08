from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('funk1/',views.funk1, name = 'funk1'),
    path('funk2/',views.funk2, name = 'funk2'),
    path('funk3/',views.funk3, name = 'funk3'),
]