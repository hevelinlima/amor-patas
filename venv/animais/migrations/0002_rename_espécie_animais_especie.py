# Generated by Django 4.2.7 on 2023-11-14 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animais',
            old_name='espécie',
            new_name='especie',
        ),
    ]
