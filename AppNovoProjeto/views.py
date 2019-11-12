from django.views.generic import TemplateView
from NovoProjeto.models import Paciente
from django.views.generic import CreateView
from django.urls.base import reverse_lazy

class Index(TemplateView):
    template_name ="index.html"
    
class CriaPaciente(CreateView): 
    template_name = "index.html"   
    model = Paciente()
    fields = '__all__'
    success_url = reverse_lazy("index")
    
class Inicio(TemplateView):
    template_name = "inicio.html"  
    
    
class Login(CreateView): 
    template_name = "login.html"   
    model = Paciente()
    fields = '__all__'
    success_url = reverse_lazy("index")    
    
    
    
    
