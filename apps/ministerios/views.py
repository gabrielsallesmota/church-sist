from django.shortcuts import render, redirect
from apps.ministerios.models import Codigo_Ministerio
from apps.ministerios.forms import MinisterioForm


def ministerio_consult(request):
    ministerios = Codigo_Ministerio.objects.all()
    return render(request, 'ministerios/consulta-ministerio.html', {'ministerios': ministerios})


def ministerio_create(request):
    if request.method == 'POST':
        form = MinisterioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ministerio_consult')
    else:
        form = MinisterioForm()
    return render(request, 'ministerios/cadastro-ministerio.html', {'form': form})


def ministerio_update(request, pk):
    ministerio = Codigo_Ministerio.objects.get(pk=pk)
    if request.method == 'POST':
        form = MinisterioForm(request.POST, instance=ministerio)
        if form.is_valid():
            form.save()
            return redirect('ministerio_consult')
    else:
        form = MinisterioForm(instance=ministerio)
    return render(request, 'ministerios/editar-ministerio.html', {'form': form, 'ministerio': ministerio})


def ministerio_delete(request, pk):
    ministerio = Codigo_Ministerio.objects.get(pk=pk)
    if request.method == 'POST':
        ministerio.delete()
        return redirect('ministerio_consult')
    return render(request, 'ministerios/excluir-ministerio.html', {'ministerio': ministerio})


def generate_ministerios_report(request):
    filtro_nome = request.GET.get('filtro_nome', '')

    ministerios = Codigo_Ministerio.objects.all()

    if filtro_nome:
        ministerios = ministerios.filter(ministerio__icontains=filtro_nome)

    context = {
        'ministerios': ministerios,
        'filtro_nome': filtro_nome,
    }

    return render(request, 'ministerios/reports_ministerios.html', context)