# Generated by Django 5.1.6 on 2025-02-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sca', '0002_alter_usuario_login_alter_usuario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='situacao',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo'), ('S', 'Suspenso'), ('O', 'outro')], max_length=1),
        ),
    ]
