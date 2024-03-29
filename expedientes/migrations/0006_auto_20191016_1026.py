# Generated by Django 2.2.6 on 2019-10-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0005_auto_20191016_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='autorizo_tapado',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='caudal',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='construyo',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='estado',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='fecha_de_instalacion',
            field=models.DateTimeField(default=None, verbose_name='Fecha de instalacion'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='inspeciono',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='medidor_marca',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='medidor_no',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='expediente',
            name='numero_de_cuenta',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='expediente',
            name='numero_de_partida',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='expediente',
            name='realizo',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='solicita_servicio_de',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='expediente',
            name='tipo',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
