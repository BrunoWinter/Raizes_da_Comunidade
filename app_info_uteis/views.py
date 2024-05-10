from django.shortcuts import render, HttpResponse

# Create your views here.
def informacoes(request):
    return render(request, 'info-uteis/info-uteis.html')