from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
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
    
@login_required(login_url="/login/login")    
def topico(request, pk):
    lista_comentários = {}
    nome_topico = get_object_or_404(Topico, pk=pk)
    try:
        lista_comentários = Comentario.objects.filter(topico=nome_topico)
        return render(request, "forum/topico.html", {'nome_topico': nome_topico, 'comentarios' : lista_comentários})
    except Comentario.DoesNotExist:
        return render(request, "forum/topico.html")
    

    
@login_required(login_url="/login/login")
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

@login_required(login_url="/login/login")
def criar_comentario(request, topico_id):
    if request.method == "POST":
        usuario = request.user
        topico = get_object_or_404(Topico, pk=topico_id)
        
        comentario = request.POST.get("comentario")
        
        novo_comentario = Comentario(usuario=usuario, comentario=comentario, topico=topico)
        novo_comentario.save()
        return redirect("topico", pk=topico_id)
    else:
        return render(request, "forum/topico.html")
    