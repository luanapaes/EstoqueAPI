from django.db import models

from empresa.models import Empresa

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from estoque_project import settings
  
class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

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
        # Gerar um nome de usuário único baseado no nome do funcionário
        base_username = instance.nome.lower().replace(' ', '_')
        username = base_username
        suffix = 1
        while User.objects.filter(username=username).exists():
            # Se já existir um usuário com o mesmo nome de usuário, adicionar um número ao final
            username = f"{base_username}_{suffix}"
            suffix += 1

        if instance.tipo == "ADM":
            user = User.objects.create_superuser(
                username=username,
                email=instance.email,
                password=instance.senha,
            )
        elif instance.tipo == "FUNC":
            user = User.objects.create_user(
                username=username,
                email=instance.email,
                password=instance.senha,
            )
        return user


post_save.connect(create_user_from_funcionario, sender=Funcionario)

