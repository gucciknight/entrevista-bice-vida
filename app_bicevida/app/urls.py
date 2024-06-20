from django.urls import path
from .views import AppView

urlpatterns = [
    path('app/', AppView.as_view(), name='app'),
]

