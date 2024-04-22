from django.shortcuts import render, HttpResponse

# Create your views here.
def cultivo(request):
    return render(request, 'cultivo/cultivo.html')