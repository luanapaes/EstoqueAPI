from django.contrib.auth.hashers import make_password
from empresa.models import Empresa

from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10, choices=[
        ('ADM', 'Administrador'), ('FUNC', 'Funcionário Comum')])
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome_empresa = models.CharField(max_length=255, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.senha = make_password(self.senha)
    #     super().save(*args, **kwargs) #-- criptografia da senha

# se for tipo ADM criar super, se tipo FUNC tipo comum
# FUNC = funcionário
def create_user_from_funcionario(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == "ADM":
            user = User.objects.create_superuser(
                username=instance.nome,
                email=instance.email,
                password=instance.senha,
            )
        elif instance.tipo == "FUNC":
            user = User.objects.create_user(
                username=instance.nome,
                email=instance.email,
                password=instance.senha,
            )


post_save.connect(create_user_from_funcionario, sender=Funcionario)


