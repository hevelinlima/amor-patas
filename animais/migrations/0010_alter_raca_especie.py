# Generated by Django 4.2.7 on 2023-11-23 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0009_animais_cirurgias_animais_medicacoes_atuais_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raca',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animais.especies'),
        ),
    ]