from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models  import Comentario, Topico

@login_required(login_url="/login/login")
def forum(request):
    lista_topicos = {}
    try:
        lista_topicos = Topico.objects.all()
        return render(request, "forum/forum.html", {'topicos' : lista_topicos})
    except Topico.DoesNotExist:
        return render(request, "forum/forum.html")
    

def criar_topico(request):
    if request.method == "POST":
        usuario = request.user
        nome = request.POST.get("nomeTopico")
        descricao = request.POST.get("textoTopico")
        novo_topico = Topico(criador=usuario,titulo=nome,descricao=descricao)
        novo_topico.save()
        return redirect("forum")
    else:
        return render(request, "forum/forum.html")