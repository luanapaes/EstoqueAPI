# Generated by Django 5.0.4 on 2024-05-09 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0006_funcionario_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='username',
        ),
    ]
