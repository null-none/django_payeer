# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import payment_systems.payeer.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PSForUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('wallet', models.CharField(validators=[payment_systems.payeer.models.validate_payeer_wallet], blank=True, verbose_name='Payeer wallet', null=True, max_length=8, db_index=True, default=None)),
                ('balance', models.DecimalField(max_digits=8, default=0, decimal_places=2, verbose_name='Balance')),
                ('user', models.OneToOneField(related_name='payeer', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'payeer',
                'verbose_name': 'payeer',
            },
            bases=(models.Model,),
        ),
    ]
