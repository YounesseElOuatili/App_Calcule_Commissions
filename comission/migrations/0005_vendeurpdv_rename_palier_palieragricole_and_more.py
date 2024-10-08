# Generated by Django 5.0.7 on 2024-08-01 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comission', '0004_alter_palier_external_id_alter_palier_qte_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendeurPdv',
            fields=[
                ('external_id_v', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Référence')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du Vendeur')),
            ],
            options={
                'verbose_name': 'Vendeur PDV',
                'db_table': 'vendeur_pdv',
                'ordering': ['external_id_v'],
            },
        ),
        migrations.RenameModel(
            old_name='Palier',
            new_name='PalierAgricole',
        ),
        migrations.RenameModel(
            old_name='Vendeur',
            new_name='VendeurAgricole',
        ),
        migrations.AlterModelOptions(
            name='palieragricole',
            options={'ordering': ['external_id'], 'verbose_name': 'Palier Agricole'},
        ),
        migrations.AlterModelOptions(
            name='vendeuragricole',
            options={'ordering': ['external_id_v'], 'verbose_name': 'Vendeur Agricole'},
        ),
        migrations.AlterModelTable(
            name='palieragricole',
            table='palier_agricole',
        ),
        migrations.AlterModelTable(
            name='vendeuragricole',
            table='vendeur_agricole',
        ),
        migrations.CreateModel(
            name='PalierPdv',
            fields=[
                ('external_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Référence')),
                ('qte', models.IntegerField(blank=True, null=True, verbose_name='Quantité')),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='Total')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('vendeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comission.vendeurpdv', verbose_name='Vendeur')),
            ],
            options={
                'verbose_name': 'Palier PDV',
                'db_table': 'palier_pdv',
                'ordering': ['external_id'],
            },
        ),
    ]
