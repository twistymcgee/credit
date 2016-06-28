from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /reconsyl/
    url(r'^$', views.index, name='index'),
    # ex: /reconsyl/5/
    url(r'^(?P<account_id>[0-9]+)/$', views.account, name='account'),
    # ex: /reconsyl/5/ledger/
    url(r'^(?P<account_id>[0-9]+)/ledger/$', views.ledger, name='ledger'),
]
