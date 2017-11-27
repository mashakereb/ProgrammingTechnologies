from .models import Account
from .models import Payment
from django.db import transaction
from decimal import Decimal
from . import errors


def deposit(account_id, amount):
    with transaction.atomic():
        account = (
            Account.objects.select_for_update().get(id=account_id)
        )

        account.balance += amount
        account.save()

        payment = Payment(account_id=account_id, type=Payment.Deposit, amount=amount)
        payment.save()

        return payment


def withdraw(account_id, amount):
    with transaction.atomic():
        account = (
            Account.objects.select_for_update().get(id=account_id)
        )

        if account.balance < amount:
            raise Exception(errors.INSUFFICIENT_FUNDS)

        account.balance -= amount
        account.save()

        payment = Payment(account_id=account_id, type=Payment.Withdrawal, amount=amount)
        payment.save()

        return payment


def make_payment(type, account_id, amount):
    if type == Payment.Withdrawal:
        return withdraw(account_id, Decimal(amount))
    else:
        return deposit(account_id, Decimal(amount))


def block_account(account):
    account.is_blocked = True
    account.save()


def is_account_owner(account, user):
    return account.card.profile.user.id == user.id
