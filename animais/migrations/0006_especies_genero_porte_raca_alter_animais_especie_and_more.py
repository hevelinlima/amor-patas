# Generated by Django 4.2.7 on 2023-11-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0005_animais_genero_animais_vacinacao_em_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Porte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('descrição', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='animais',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animais.especies'),
        ),
        migrations.AlterField(
            model_name='animais',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animais.genero'),
        ),
        migrations.AlterField(
            model_name='animais',
            name='porte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animais.porte'),
        ),
        migrations.AlterField(
            model_name='animais',
            name='raça',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animais.raca'),
        ),
    ]