from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Payment, Account, CreditCard


class AccountSerializer(ModelSerializer):
    """
    DRF serializer for account model
    """
    class Meta:
        model = Account
        fields = '__all__'


class CreditCardSerializer(ModelSerializer):
    """
    DRF serializer for credit card model
    """
    account = AccountSerializer(read_only=True)

    class Meta:
        model = CreditCard
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    """
    DRF serializer for payment model
    """
    account = PrimaryKeyRelatedField(queryset=Account.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
