# Generated by Django 2.2.13 on 2020-10-19 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_connector', '0037_auto_20201018_1628'),
        ('django_eveonline_doctrine_manager', '0010_auto_20201016_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evedoctrinesettings',
            options={'verbose_name': 'Doctrine Settings', 'verbose_name_plural': 'Doctrine Settings'},
        ),
        migrations.CreateModel(
            name='EveFittingMarketRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_stock', models.IntegerField()),
                ('fitting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_eveonline_doctrine_manager.EveFitting')),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_eveonline_connector.EveStructure')),
            ],
        ),
    ]
