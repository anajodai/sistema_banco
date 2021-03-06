from django.db import models


class Pessoa(models.Model):

  GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
  )

  nome = models.CharField(
    max_length=255, 
    verbose_name='Nome'
  )

  cpf = models.CharField(
    max_length=14, 
    verbose_name='CPF'
  )

  email = models.EmailField(
    max_length=255, 
    verbose_name='E-mail'
  )
  telefone = models.CharField(
    max_length=255, 
    verbose_name='Celular'
    )

  genero = models.CharField(
    max_length=255, 
    verbose_name='Gênero', choices=GENEROS
    )

  ativo = models.BooleanField(
    default= True
  )

  data_de_criacao = models.DateField(
    auto_now_add=True
  )

  def __str__(self):
    return self.nome+ ' ' + self.email

class Conta(models.Model):
  pessoa = models.ForeignKey(
    Pessoa, on_delete=models.CASCADE
  )
  numero_conta = models.CharField(
    max_length=255,
    verbose_name='Número da conta'
  )

  saldo = models.FloatField(
    default=0.0
  )

  agencia = models.CharField(
    max_length=255,
    verbose_name='Agência'
  )

  nome_banco = models.CharField(
    max_length=255,
    verbose_name='Nome do Banco',
    default='DogBank',
    null=True
  )

  
