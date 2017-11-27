from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver


class CreditCard(models.Model):

    Visa = 'Visa'
    MasterCard = 'MasterCard'

    CardTypes = (
        (Visa, Visa),
        (MasterCard, MasterCard),
    )

    number = models.DecimalField(
        max_digits=16,
        decimal_places=0,
        verbose_name=_('Number'),
        unique=True
    )

    expiration_date = models.DateField(
        verbose_name=_('Expiration date')
    )

    type = models.TextField(
        choices=CardTypes
    )
    profile = models.ForeignKey(
        'authentication.Profile',
        related_name='cards',
    )

    @property
    def str_number(self):
        str_number = str(self.number)
        return '-'.join([str_number[i:i+4] for i in range(0, 13, 4)])


class Account(models.Model):
    balance = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name=_('Balance'),
    )

    is_blocked = models.BooleanField(
        verbose_name=_('Is the account blocked for financial transactions'),
        default=False
    )

    card = models.OneToOneField(
        CreditCard,
        verbose_name=_('CreditCard'),
        related_name='account'
    )


class Payment(models.Model):
    Withdrawal = 'Withdrawal'
    Deposit = 'Deposit'

    PaymentTypes = (
        (Withdrawal, 'Withdrawal'),
        (Deposit, 'Deposit'),
    )

    type = models.TextField(
        verbose_name=_('Type'),
        choices=PaymentTypes
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=0,
    )
    account = models.ForeignKey(
        Account,
        related_name="payments",
    )

    created = models.DateTimeField(
        verbose_name=_('Payment date'),
        auto_now=True
    )


@receiver(post_save, sender=CreditCard)
def create_profile(sender, instance, created, **kwargs):
    """
    Create  account after card create
    """
    if created:
        Account.objects.create(card=instance)


@receiver(post_save, sender=CreditCard)
def save_user_profile(sender, instance, **kwargs):
    """
    Update  account after card update
    """
    instance.account.save()
