from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Evento
from .forms import EventoForm
from datetime import datetime

def evento_list(request):
    evento = Evento.objects.all()
    return render(request, 'eventos/consulta-evento.html', {'evento': evento})


def evento_create(request):
    form = EventoForm
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Novo Evento Cadastrado!")
            return redirect('evento_list')

    return render(request, 'eventos/criar-evento.html', {'form': form})


def evento_update(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    form = EventoForm(instance=evento)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    return render(request, 'eventos/editar-evento.html', {'form': form, 'evento': evento})


def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'eventos/excluir-evento.html', {'evento': evento})


def generate_eventos_report(request):
    filtro_campo = request.GET.get('filtro_campo', '')
    filtro_valor = request.GET.get('filtro_valor', '')
    
    eventos = Evento.objects.all()

    if filtro_campo == 'nome_evento':
        eventos = eventos.filter(nome_evento__icontains=filtro_valor)

    context = {
        'eventos': eventos,
        'filtro_campo': filtro_campo,
        'filtro_valor': filtro_valor,
    }
    
    return render(request, 'eventos/reports-evento.html', context)