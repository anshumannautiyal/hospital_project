# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noon_report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.TextField(null=True)),
                ('cons', models.TextField(null=True)),
                ('speed', models.TextField(null=True)),
                ('currents', models.TextField(null=True)),
                ('winds', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ship_record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('last_service', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ship_voyage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voyage_no', models.TextField(null=True)),
                ('ship', models.ForeignKey(to='hospital_recors.ship_record')),
            ],
        ),
        migrations.AddField(
            model_name='noon_report',
            name='voyage',
            field=models.ForeignKey(to='hospital_recors.ship_voyage'),
        ),
    ]
