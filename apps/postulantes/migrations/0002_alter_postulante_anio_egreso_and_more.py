# Generated by Django 4.1.5 on 2024-03-12 13:59

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante',
            name='anio_egreso',
            field=models.PositiveIntegerField(max_length=8, verbose_name='Año_egreso'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='imagen1',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps', verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='imagen2',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps', verbose_name='Certificado de Estudios'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='imagen3',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps', verbose_name='Partida de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='imagen4',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps', verbose_name='Voucher'),
        ),
    ]
