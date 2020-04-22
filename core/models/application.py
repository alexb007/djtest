from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Application(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name=_('Application name')
    )
    api_key = models.CharField(
        max_length=256,
        verbose_name=_('API Key')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is application active?')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Created at')
    )

    def create_apikey(self):
        import secrets
        self.api_key = secrets.token_hex(32)
        self.save(update_fields=['api_key'])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

@receiver(post_save, sender='core.Application', dispatch_uid="post_app_save")
def post_app_save(sender, instance, created, **kwargs):
    if created:
        instance.create_apikey()
