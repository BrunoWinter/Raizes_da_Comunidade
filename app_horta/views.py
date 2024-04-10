from django.shortcuts import render, redirect
from .models import Horta
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login/login/")
def minha_horta(request):
    try:
        horta_do_usuario = Horta.objects.get(usuario=request.user)
        return render(request, 'horta/horta.html', {'horta': horta_do_usuario})
    except Horta.DoesNotExist:
        return render(request, 'horta/horta.html')
    
    
@login_required
def criar_horta(request):
    if request.method == "POST":
       nome = request.POST.get('nome')
       descricao = request.POST.get('descricao')
       nova_horta = Horta(usuario= request.user, nome=nome,descricao=descricao)
       nova_horta.save()
       return redirect("minha_horta")
    else:
        return render(request, 'horta/criar_horta.html')

