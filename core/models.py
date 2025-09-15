from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

user = get_user_model()

#TextChoices
class GencerChoice(models.TextChoices):
    MALE = 'M', _('Masculino')
    FEMALE = 'F', _('Feminino')


class TypeChoice(models.TextChoices):
    BUSINESS = 'B', _('Pessoa Jurídica')
    PERSON = 'P', _('Pessoa Física')


# Mixin
class TimeStamp(models.Model):
    created = models.DateTimeField(_("criado em"), auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        user, 
        verbose_name=_("criado por"),
        related_name="user_created_by",
        related_query_name='quser_created_by',
        on_delete=models.DO_NOTHING,
    )
    modified = models.DateTimeField(_("modificado em"), auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(
        user, 
        verbose_name=_("modificado por"),
        related_query_name='quser_modified_by',
        related_name="user_modified_by",
        on_delete=models.DO_NOTHING,
    )
    
    class Meta:
        abstract = True
        