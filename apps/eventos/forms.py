from django import forms
from apps.eventos.models import Evento, InscricaoEvento
from apps.membros.models import Membros


class EventoForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(
        queryset=Membros.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Responsável"
    )

    class Meta:
        model = Evento
        exclude = ['id']
        labels = {
            'nome_evento': 'Nome do Evento:',
            'data_evento': 'Data do Evento:'
        }
        widgets = {
            'nome_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'data_evento': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control', 'input_formats': ['%Y-%m-%d']})
        }


class InscricaoEventoForm(forms.ModelForm):
    class Meta:
        model = InscricaoEvento
        exclude = ['id']
        labels = {
            'membro_participante': 'Membro:',
            'data': 'Data de Incricão:',
        }
        widgets = {
            'membro': forms.Select(attrs={'class': 'form-control'}),
            'data_evento': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control', 'input_formats': ['%Y-%m-%d']})
        }
