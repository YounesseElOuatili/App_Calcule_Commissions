# Generated by Django 4.2.3 on 2024-07-24 16:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0007_rename_historicalsociete_historicalsocietee_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalSocietee',
            new_name='HistoricalSociete',
        ),
        migrations.RenameModel(
            old_name='Societee',
            new_name='Societe',
        ),
        migrations.AlterModelOptions(
            name='historicalsociete',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical societe', 'verbose_name_plural': 'historical Sociétés'},
        ),
    ]
