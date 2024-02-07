from django.shortcuts import render

def index(resquest):
    return render(resquest, "galeria\index.html")

def imagem(resquest):
    return render(resquest, "galeria\imagem.html")
