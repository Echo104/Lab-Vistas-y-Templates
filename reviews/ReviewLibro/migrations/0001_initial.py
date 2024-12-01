# Generated by Django 5.1.3 on 2024-11-24 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReviewLibro.libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReviewLibro.usuario')),
            ],
        ),
    ]