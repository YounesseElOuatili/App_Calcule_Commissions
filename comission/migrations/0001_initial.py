# Generated by Django 5.0.7 on 2024-07-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paliers',
            fields=[
                ('external_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Reference')),
                ('qte', models.IntegerField(blank=True, null=True, verbose_name='Quantite')),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='Total')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Paliers',
                'db_table': 'paliers_paliers',
                'ordering': ['external_id'],
            },
        ),
        migrations.CreateModel(
            name='Vendeurs',
            fields=[
                ('external_id_v', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Reference')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom Vendeurs')),
            ],
            options={
                'verbose_name': 'Vendeurs',
                'db_table': 'vendeurs_vendeurs',
                'ordering': ['external_id_v'],
            },
        ),
    ]
