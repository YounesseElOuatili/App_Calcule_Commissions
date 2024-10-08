# Generated by Django 4.2.3 on 2024-07-24 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_historicalsite_availability_check_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalperimeter_category',
            name='history_user',
        ),
        migrations.AlterUniqueTogether(
            name='perimeter',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='perimeter',
            name='category',
        ),
        migrations.RemoveField(
            model_name='perimeter',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='perimeter',
            name='site',
        ),
        migrations.RemoveField(
            model_name='sitesequences',
            name='site',
        ),
        migrations.RemoveField(
            model_name='historicalsite',
            name='default_perimeter',
        ),
        migrations.RemoveField(
            model_name='site',
            name='default_perimeter',
        ),
        migrations.DeleteModel(
            name='HistoricalPerimeter',
        ),
        migrations.DeleteModel(
            name='HistoricalPerimeter_Category',
        ),
        migrations.DeleteModel(
            name='Perimeter',
        ),
        migrations.DeleteModel(
            name='Perimeter_Category',
        ),
        migrations.DeleteModel(
            name='SiteSequences',
        ),
    ]
