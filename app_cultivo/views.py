from django.shortcuts import render, HttpResponse

from app_cultivo.models import Cultivo

# Create your views here.
def cultivo(request):
    lista_cultivos = {}

    lista_cultivos['cultivos'] = Cultivo.objects.all()

    return render(request, 'cultivo/cultivo.html', lista_cultivos)


def pesquisa(request):
    query = request.GET.get('q')
    resultado = Cultivo.objects.filter(nome__icontains = query)
    return render(request, 'cultivo/busca.html', {'resultados': resultado})