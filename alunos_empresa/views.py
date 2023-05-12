from django.shortcuts import render, HttpResponse, redirect
from alunos_empresa.models import Usuario

# Create your views here.

def index(request):
    return redirect ('/cemp')

def lista(request):
    usuario = Usuario.objects.all()
    dados = {'usuarios':usuario}
    return render(request, 'cemp.html', dados)

     
