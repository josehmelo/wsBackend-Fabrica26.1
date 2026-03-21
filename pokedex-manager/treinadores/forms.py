from django import forms
from .models import Treinador


class TreinadorForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Treinador
        fields = ['nome', 'idade', 'email', 'senha']