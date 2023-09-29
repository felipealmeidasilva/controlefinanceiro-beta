from django import forms
from .models import Contato, Cadastro

class ContatoForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = '__all__'

class CadastrarForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ['data', 'responsavel','descricao','tipo', 'valor', 'comprovante']

        widgets = {
            'data' : forms.SelectDateWidget()
        }