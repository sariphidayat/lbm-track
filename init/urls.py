from django.urls import path

from .views import protected_view


urlpatterns = [
    path('hello/', protected_view, name='hello'),
]
