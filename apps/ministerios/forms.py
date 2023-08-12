from django import forms
from apps.ministerios.models import Codigo_Ministerio
from apps.membros.models import Membros


class MinisterioForm(forms.ModelForm):
    lider = forms.ModelChoiceField(queryset=Membros.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Codigo_Ministerio
        exclude = ['id']
        labels = {
            'ministerio': 'Ministério:',
            'lider': 'Líder:',
            'situacao': 'Situação:',
        }
        widgets = {
            'ministerio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do Ministério'}),
            'situacao': forms.Select(attrs={'class': 'form-control'}),
        }
