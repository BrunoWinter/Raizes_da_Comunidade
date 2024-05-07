from django.shortcuts import render, redirect, get_object_or_404
from .models import Horta, Cultura
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login/login/")
def minha_horta(request):
    lista_culturas = {}
    try:
        horta_do_usuario = Horta.objects.get(usuario=request.user)
        horta_id = horta_do_usuario.id
        lista_culturas = Cultura.objects.filter(horta_id=horta_id)
        return render(request, 'horta/horta.html', {'horta': horta_do_usuario, 'culturas': lista_culturas})
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
    
    
@login_required
def inserir_cultura(request):
    
    if request.method == 'POST':
        horta_usuario = Horta.objects.get(usuario=request.user)
        horta_id=horta_usuario.id

        nome = request.POST.get('nome_cultura')
        tipo = request.POST.get('tipo_cultura')
        descricao = request.POST.get('desc_cultura')
        
        nova_cultura = Cultura(horta_id= horta_id, name=nome, type=tipo, desc=descricao)

        nova_cultura.save()
        
        return redirect('minha_horta')
    
    return render(request, "horta/horta.html")

@login_required
def excluir_cultura(request, pk):
    if request.method == 'POST':
        cultura = get_object_or_404(Cultura, pk=pk)
        cultura.delete()
        return redirect('minha_horta')
    else:
        return redirect('minha_horta')

        

