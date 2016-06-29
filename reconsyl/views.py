from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic

from .models import Account, Transact
from .forms import TransactForm


class IndexView(generic.ListView):
    template_name = 'reconsyl/index.html'
    context_object_name = 'account_list'

    def get_queryset(self):
        return Account.objects.order_by('name_text')

def transact(request, transact_id):
    transact = get_object_or_404(Transact, pk=transact_id)
    form = TransactForm(instance=transact)
    return render(request, 'reconsyl/transact.html', {'transact': transact, 'form': form})

def account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'reconsyl/account.html', {'account': account})

def ledger(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'reconsyl/ledger.html', {'account': account})
