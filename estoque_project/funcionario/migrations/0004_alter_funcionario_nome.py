# Generated by Django 5.0.4 on 2024-04-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_funcionario_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
