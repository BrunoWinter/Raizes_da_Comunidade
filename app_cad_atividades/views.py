from django.shortcuts import render
from .models import Atividade
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request, "./home.html")

@login_required(login_url="/login/login/")
def atividades(request):
    lista_atividades = {}
    
    if request.method == 'POST':
        atividade = request.POST.get("atividade")
        dt_atividade = request.POST.get("dt_atividade")
        usuario_id = request.user.username
        nova_atividade = Atividade(atividade=atividade, dt_atividadedb=dt_atividade ,usuario_id=usuario_id )
        nova_atividade.save()
                    
    lista_atividades["atividades"] = Atividade.objects.all().order_by('-dt_atividadedb')[:10]
    
    return render(request, "atividades/atividade.html", lista_atividades)