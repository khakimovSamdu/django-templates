from django.urls import path
from .views import RegistratsiyaPage

urlpatterns = [
    path('register/', RegistratsiyaPage.as_view()),
]