from django.urls import path
from . import views

urlpatterns = [
    path('personagens/', views.exibir_personagens, name='exibir_personagens'),
]
