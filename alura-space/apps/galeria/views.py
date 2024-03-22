from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Photograph
from apps.galeria.forms import PhotographForm

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    
    photographs = Photograph.objects.order_by("-created").filter(published=True)
    known_categories = [category[-1] for category in Photograph.CATEGORY_OPTIONS]

    return render(request, r"galeria/index.html", {"cards": photographs, "categories": known_categories})

def imagem(request, photograph_id):
    photograph = get_object_or_404(Photograph, pk=photograph_id)
    return render(request, r"galeria/imagem.html", {"photograph": photograph})

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

    known_categories = [category[-1] for category in Photograph.CATEGORY_OPTIONS]

    return render(request, r"galeria/index.html", {"cards": macthed_photographs, "categories": known_categories})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')
    
    form = PhotographForm()
    if request.method == 'POST':
        form = PhotographForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Nova fotografia cadastrada.")
            return redirect('index')
    
    return render(request, r"galeria/nova_imagem.html", {'form': form})

def editar_imagem(request, photograph_id):
    photograph = get_object_or_404(Photograph, pk=photograph_id)
    form = PhotographForm(instance=photograph)

    if request.method == 'POST':
        form = PhotographForm(request.POST, request.FILES, instance=photograph)
        if form.is_valid():
            form.save()
            messages.success(request, "Alterações salvas.")
            return redirect('index')

    return render(request, r"galeria/editar_imagem.html", {'form': form, "photograph": photograph})

def deletar_imagem(request, photograph_id):
    photograph = get_object_or_404(Photograph, pk=photograph_id)

    if photograph:
        photograph.delete()
        messages.success(request, "Fotografia deletada.")

    return redirect('index')

def filtro(request, category):

    photographs = Photograph.objects.order_by("created").filter(published=True, category=category)
    known_categories = [category[-1] for category in Photograph.CATEGORY_OPTIONS]

    return render(request, r"galeria/index.html", {"cards": photographs, "categories": known_categories})