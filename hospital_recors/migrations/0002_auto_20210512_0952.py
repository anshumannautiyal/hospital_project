# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_recors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship_voyage',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital_recors.ship_record', null=True),
        ),
    ]
