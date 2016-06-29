from django.conf.urls import url

from . import views

app_name = 'reconsyl'
urlpatterns = [
    # ex: /reconsyl/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /reconsyl/5/
    url(r'^(?P<account_id>[0-9]+)/$', views.account, name='account'),
    # ex: /reconsyl/5/ledger/
    url(r'^(?P<account_id>[0-9]+)/ledger/$', views.ledger, name='ledger'),
    # ex: /reconsyl/transact/3/
    url(r'^transact/(?P<transact_id>[0-9]+)/$', views.transact, name='transact'),
]
