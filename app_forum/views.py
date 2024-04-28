from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/login")
def forum(request):
    return render(request, "forum/forum.html")