from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForm, CadastroForm
from django.contrib import auth, messages
from django.contrib.auth.models import User

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            nome = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect("index")
            else:
                messages.error(request, "Erro ao efeturar login.")

        return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForm()

    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            
            nome_cadastro = form["nome_cadastro"].value()
            email_cadastro = form["email_cadastro"].value()
            senha_cadastro = form["senha_1"].value()

            if User.objects.filter(username=nome_cadastro).exists():
                messages.error(request, "Usuário já existente.")
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=nome_cadastro,
                email=email_cadastro,
                password=senha_cadastro
            )
            usuario.save()
            messages.success(request, f"{nome_cadastro} cadastrado com sucesso!")
            return redirect("login")
    
    return render(request, "usuarios/cadastro.html", {"form": form})
    
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso.")
    return redirect("login")

