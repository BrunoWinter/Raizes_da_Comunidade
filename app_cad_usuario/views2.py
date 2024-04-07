from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
 
def cadastro(request):
    if request.method == "GET":
        return render(request, "usuario/cadastro.html")
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=usuario).first()
        if user:
            return render(request, "usuario/cadastro.html", {'error_message': 'Usuário já cadastrado'})
            
        
        user = User.objects.create_user(username=usuario, password=senha)
        user.save()
        
        
        return render(request, "usuario/cadastro.html", {'sucessful_message': 'Usuário cadastrado com sucesso'} )
        
            