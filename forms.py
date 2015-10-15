from django import forms
from django.utils.translation import ugettext_lazy as _


class PSForUserDefaultForm(forms.ModelForm):
    class Meta:
        fields = ('wallet',)

    def clean_wallet(self):
        retval = self.cleaned_data['wallet']
        if self.instance.wallet and 'wallet' in self.changed_data:
            raise forms.ValidationError(_('Изменение кошелька запрещено в целях безопасности'))
        return retval
