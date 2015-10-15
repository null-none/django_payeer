from django import forms
from .models import PSForUser
from django_payeer.forms import PSForUserDefaultForm


class PSForUserForm(PSForUserDefaultForm):
    class Meta:
        model = PSForUser
        fields = ('wallet',)

