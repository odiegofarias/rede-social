from email.message import Message
from socket import fromshare
from django import forms
from .models import Mensagem


class MessageForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Digite algo...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )


    class Meta:
        model = Mensagem
        exclude = ("user",)