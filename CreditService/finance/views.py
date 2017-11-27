from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from .models import Account
from .serializers import PaymentSerializer
from django.core.exceptions import PermissionDenied
from . import services


@login_required()
def get_cards(request):
    return render(request, 'cards.html', {'cards': request.user.profile.cards.all()})


@login_required()
def get_payments(request, account_id):
    account = Account.objects.get(id=account_id)
    if not services.is_account_owner(account, request.user):
        raise PermissionDenied()
    return render(request, 'payments.html', {'payments': account.payments.all(), 'account': account})


@login_required()
def block_account(request, account_id):
    account = Account.objects.get(id=account_id)
    if not services.is_account_owner(account, request.user):
        raise PermissionDenied()
    services.block_account(account)
    return render(request, 'cards.html', {'cards': request.user.profile.cards.all()})


@login_required()
def create_payment(request, account_id):
    serializer = PaymentSerializer(data=request.POST)
    account = Account.objects.get(id=account_id)
    errors = []

    if not services.is_account_owner(account, request.user):
        raise PermissionDenied()
    try:
        if serializer.is_valid():
            data = serializer.data
            payment_type = data['type']
            amount = data['amount']
            services.make_payment(payment_type, account_id, amount)
            return redirect('/payments/' + str(account_id))
    except Exception as e:
        errors.append(str(e))
    return render(request, 'payments.html',
                  {'form': {'data': serializer.initial_data, 'errors': errors},
                   'payments': account.payments.all(),
                   'account': account,
                  })
