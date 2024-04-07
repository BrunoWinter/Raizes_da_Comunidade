from django.shortcuts import render
from .models import Atividade
from datetime import datetime

def home(request):
    return render(request, "./home.html")

def atividades(request):
    lista_atividades = {}
    
    if request.method == 'POST':
        atividade = request.POST.get("atividade")
        dt_atividade = request.POST.get("dt_atividade")
        nova_atividade = Atividade(atividade=atividade, dt_atividade=dt_atividade)
        nova_atividade.save()
                    
    lista_atividades["atividades"] = Atividade.objects.all().order_by('-dt_atividade')[:10]
    
    return render(request, "atividades/atividade.html", lista_atividades)