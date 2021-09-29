# Generated by Django 3.2.6 on 2021-09-08 00:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.IntegerField(verbose_name='Código Postal')),
            ],
            options={
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('num_doc', models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='Número de Documento')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=150)),
                ('num_cuit', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número de CUIT/CUIL')),
                ('fecha_nac', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=50, verbose_name='Número de teléfono')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('direccion', models.CharField(max_length=120, verbose_name='Dirección')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='persona_localidad', to='odontologia.localidad')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=8, verbose_name='Contraseña')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_persona', to='odontologia.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('num_hc', models.IntegerField(primary_key=True, serialize=False, verbose_name='Número de historia clínica')),
                ('num_os', models.IntegerField(blank=True, null=True, verbose_name='Número de Obra Social')),
                ('titular_familiar', models.BooleanField(verbose_name='¿Titular?')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.persona')),
            ],
        ),
    ]