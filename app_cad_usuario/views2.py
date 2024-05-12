from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
        
        
        return render(request, "usuario/login.html", {'sucessful_message': 'Usuário cadastrado com sucesso'} )
        
            
def user_login(request):
    if request.method == "GET":
        return render(request, 'usuario/login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return render(request, "home.html", {'sucessful_message': 'Usuário Logado com sucesso'} )
            #return HttpResponse('autenticado')
        else:
            lista_mensagem = {}
            lista_mensagem['mensagem_erro'] = 'E-mail ou senha inválidos'
            return render(request, 'usuario/login.html', lista_mensagem)
        
def user_logout(request):
    logout(request)
    return redirect('home')