# Generated by Django 3.2.6 on 2021-09-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odontologia', '0002_profesional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='num_doc',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Número de Documento'),
        ),
    ]