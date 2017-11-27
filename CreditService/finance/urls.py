from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^cards/', views.get_cards),
    url(r'^payments/(?P<account_id>\w+)', views.get_payments),
    url(r'^payment/(?P<account_id>\w+)', views.create_payment),
    url(r'^account/block/(?P<account_id>\w+)', views.block_account),

    url(r'^i18n/', include('django.conf.urls.i18n')),
]