from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        verbose_name=_('User'),
        related_name='profile',
        related_query_name='account_email',
        on_delete=models.CASCADE
    )

    is_blocked = models.BooleanField(
        verbose_name=_('Is user blocked in system'),
        default=False
    )
    balance = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name=_('Balance')
    )

    def __str__(self):
        return '{} | balance: {}'.format(self.user.username, self.balance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create  profile after user create
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Update  profile after user update
    """
    instance.profile.save()
