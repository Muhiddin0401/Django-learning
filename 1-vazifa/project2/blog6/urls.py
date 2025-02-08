from django.urls import path
from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('funk16/', views.funk16, name = 'funk16'),
    path('funk17/', views.funk17, name = 'funk17'),
    path('funk18/', views.funk18, name = 'funk18'),
]