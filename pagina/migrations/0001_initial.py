# Generated by Django 2.2.6 on 2019-11-18 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuarios.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCurso', models.CharField(max_length=4, unique=True)),
                ('title', models.CharField(max_length=20)),
                ('credito', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.curso')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(blank=True, max_length=20)),
                ('clas', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pagina.clase')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='secc',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pagina.seccion'),
        ),
    ]
