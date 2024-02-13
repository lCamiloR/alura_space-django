from django.shortcuts import render, redirect

from usuarios.forms import LoginForm, CadastroForm
from django.contrib import auth
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
                return redirect("index")
            
        return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():

            if form["senha_1"].value() != form["senha_2"].value():
                return redirect("cadastro")
            
            nome_cadastro = form["nome_cadastro"].value()
            email_cadastro = form["email_cadastro"].value()
            senha_cadastro = form["senha_1"].value()

            if User.objects.filter(username=nome_cadastro).exists():
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=nome_cadastro,
                email=email_cadastro,
                password=senha_cadastro
            )
            usuario.save()

            return redirect("login")

    else:
        form = CadastroForm()
        return render(request, "usuarios/cadastro.html", {"form": form})

