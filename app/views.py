from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Cadastro
from .forms import ContatoForm, CadastrarForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models.aggregates import Sum

# Create your views here.
def home(request):
    cadastros = Cadastro.objects.all()
    data = {
        'cadastros' : cadastros
    }
    data['subtotal'] = 0
    return render(request, 'app/home.html', data)

def contato(request):
    data = {
        'form' : ContatoForm()
    }

    if request.method == 'POST':
        formulario = ContatoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Mensagem com sucesso!")
        else:
            data['form'] = formulario

    return render(request, 'app/contato.html', data)

def adicionar_cadastro(request):
    data = {
        'form': CadastrarForm()
    }
    
    if request.method == 'POST':
        formulario = CadastrarForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Cadastro feito com sucesso!")

        else:
            data['form'] = formulario

    return render(request, 'app/cadastro/cadastrar.html', data)

def listar_cadastro(request):
    cadastros = Cadastro.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(cadastros, 5)
        cadastros = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':cadastros,
        'paginator':paginator
    }
    return render(request, 'app/cadastro/listar.html', data)

def modificar_cadastro(request, id):

    cadastro = get_object_or_404(Cadastro, id=id)

    data = {
        'form':CadastrarForm(instance=cadastro)
    }

    if request.method == 'POST':
        formulario = CadastrarForm(data=request.POST, instance=cadastro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado com sucesso!")
            return redirect(to="listar_cadastro")
        else:
            data['form'] = formulario

    return render(request, 'app/cadastro/modificar.html', data)

def eliminar_cadastro(request, id):
    cadastro = get_object_or_404(Cadastro, id=id)
    cadastro.delete()
    messages.success(request,"Eliminado com sucesso!")
    return redirect(to="listar_cadastro")
