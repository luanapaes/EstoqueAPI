# Generated by Django 5.0.4 on 2024-04-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='nome_empresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
