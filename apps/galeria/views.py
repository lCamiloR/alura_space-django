from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Photograph
from apps.galeria.forms import PhotographForm

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    
    photographs = Photograph.objects.order_by("-created").filter(published=True)
    return render(request, r"galeria\index.html", {"cards": photographs})

def imagem(request, photograph_id):
    photograph = get_object_or_404(Photograph, pk=photograph_id)
    return render(request, r"galeria\imagem.html", {"photograph": photograph})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    
    photographs = Photograph.objects.order_by("-created").filter(published=True)
    macthed_photographs = []
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            macthed_photographs = photographs.filter(name__icontains=nome_a_buscar)

    return render(request, r"galeria\buscar.html", {"cards": macthed_photographs})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    
    form = PhotographForm()
    if request.method == 'POST':
        print("é um POST")
        form = PhotographForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            print("Form é válido")
            form.save()
            messages.success(request, "Nova fotografia cadastrada.")
            return redirect('index')
    
    return render(request, r"galeria\nova_imagem.html", {'form': form})

def editar_imagem(request):
    return render(request, r"galeria\editar_imagem.html")

def deletar_imagem(request):
    return render(request, r"galeria\deletar_imagem.html")
