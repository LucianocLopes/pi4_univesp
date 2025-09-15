from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model

from core.models import TimeStamp, TypeChoice

USER = get_user_model()


class Register(TimeStamp):

    type = models.CharField(_("Tipo de Pessoa"), max_length=1, choices=TypeChoice.choices)

    class Meta:
        verbose_name = _("Register")
        verbose_name_plural = _("Registers")

    def __str__(self):
        return self.type


class Person(Register):

    first_name = models.CharField(_("Nome"), max_length=50)
    last_name = models.CharField(_("Sobrenome"), max_length=50)
    cpf_number = models.CharField(_("CPF"), max_length=11)

    class Meta:
        verbose_name = _("Pessoa Física")
        verbose_name_plural = _("Pessoas Física")

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    
    def __str__(self):
        return self.full_name
    

class Business(Register):

    name = models.CharField(_("Razão Social"), max_length=100)
    fantasy_name = models.CharField(_("Fantasia"), max_length=100)
    cnpj_number = models.CharField(_("CNPJ"), max_length=14)

    class Meta:
        verbose_name = _("Pessoa Juridica")
        verbose_name_plural = _("Pessoas Jurídicas")
    
    def __str__(self):
        return self.name.title