from django.urls import path
from AppNovoProjeto.views import Index, Inicio, Login
from AppNovoProjeto.views import CriaPaciente
from NovoProjeto.models import Paciente

urlpatterns = [
    path('',Login.as_view(model=Paciente), name="index"), 
    path('paciente/inicio/', CriaPaciente.as_view(model=Paciente), name="index"),
]