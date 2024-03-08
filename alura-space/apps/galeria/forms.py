from django import forms
from apps.galeria.models import Photograph

class PhotographForm(forms.ModelForm):
    class Meta:
        model = Photograph
        exclude = ['published', "created", "modified"]
        labels = {
            'name': 'Nome da fotografia:',
            'legend': 'Legenda:',
            'category': 'Categoria:',
            'description': 'Descrição:',
            'file': 'Arquivo:',
            'photograph_date': 'Data da fotografia:',
            'user': 'Usuário:'
        }
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'legend': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'file': forms.FileInput(attrs={"class": "form-control"}),
            'photograph_date': forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    'type':'date',
                    "class": "form-control"
                }
            ),
            'user': forms.Select(attrs={"class": "form-control"})
        }