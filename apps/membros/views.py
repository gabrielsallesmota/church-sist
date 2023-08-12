from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.membros.models import Membros
from apps.membros.forms import MembroForms
from django.db.models import Func


def index(request):
    total_membros = Membros.get_total_membros()
    ativos = Membros.get_membros_ativos()
    inativos = Membros.get_membros_inativos()

    context = {
        'total_membros': total_membros,
        'ativos': ativos,
        'inativos': inativos,
    }
    
    return render(request, 'membros/index.html', context)


def cadastro(request):
    form = MembroForms
    if request.method == 'POST':
        form = MembroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Novo Membro Cadastrado!")
            return redirect('index')

    return render(request, 'membros/cadastro.html', {'form': form})


def consulta(request):
    filtro_nome = request.GET.get('nome', '')
    membros = Membros.objects.all()

    if filtro_nome:
        membros = membros.filter(nome_completo__icontains=filtro_nome)

    return render(request, 'membros/consulta.html', {'membros': membros, 'filtro_nome': filtro_nome})


def editar(request, id):
    membro = get_object_or_404(Membros, id=id)

    if request.method == 'POST':
        form = MembroForms(request.POST, request.FILES, instance=membro)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = MembroForms(instance=membro)

    return render(request, 'membros/editar.html', {'form': form, 'membro': membro})


def excluir(request, id):
    membro = get_object_or_404(Membros, id=id)

    if request.method == 'POST':
        membro.delete()
        return redirect('consulta')

    return render(request, 'membros/excluir.html', {'membro': membro})



def generate_membros_report(request):
    filtro_campo = request.GET.get('filtro_campo', '')
    filtro_valor = request.GET.get('filtro_valor', '')
    
    membros = Membros.objects.all()

    if filtro_campo and filtro_valor:
        query = {f'{filtro_campo}__icontains': filtro_valor}
        membros = membros.filter(**query)

    context = {
        'membros': membros,
        'filtro_campo': filtro_campo,
        'filtro_valor': filtro_valor,
    }
    
    return render(request, 'membros/reports.html', context)


def generate_aniversariantes_report(request):
    filtro_mes = request.GET.get('filtro_mes', '')
    filtro_dia = request.GET.get('filtro_dia', '')
    aniversariantes = Membros.objects.all()

    if filtro_mes:
        aniversariantes = aniversariantes.filter(data_nascimento__month=filtro_mes)

    if filtro_dia:
        aniversariantes = aniversariantes.filter(data_nascimento__day=filtro_dia)

    context = {
        'filtro_mes': filtro_mes,
        'filtro_dia': filtro_dia,
        'aniversariantes': aniversariantes,
    }
    
    return render(request, 'membros/reports_aniversario.html', context)



