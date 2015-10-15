from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import re
from django.conf import settings
from . import NAME, TITLE
from django.utils.translation import ugettext_lazy as _


def validate_payeer_wallet(wallet):
    if not re.match('P[0-9]{7}$', wallet):
        raise ValidationError(_('Кошелек должен иметь формат P1234567'))


class PSForUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Пользователь'), null=False, blank=False,
                                related_name=NAME)
    wallet = models.CharField(_('Кошелек Payeer'), default=None, null=True, blank=True, max_length=8,
                              validators=[validate_payeer_wallet], db_index=True)
    balance = models.DecimalField(_('Баланс'), default=0, null=False, blank=False, max_digits=8,
                                  decimal_places=2)

    class Meta:
        verbose_name = 'payeer'
        verbose_name_plural = 'payeer'

    def __str__(self):
        return '{} = ${}'.format(self.wallet, self.balance)

    @property
    def get_name(self):
        return NAME

    @property
    def get_title(self):
        return TITLE
