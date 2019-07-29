# Generated by Django 2.1.7 on 2019-07-29 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_conta', models.CharField(max_length=255, verbose_name='Número da conta')),
                ('saldo', models.FloatField(default=0.0)),
                ('agencia', models.CharField(max_length=255, verbose_name='Agência')),
                ('nome_banco', models.CharField(default='Bradesco', max_length=255, null=True, verbose_name='Nome do Banco')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Pessoa')),
            ],
        ),
    ]
