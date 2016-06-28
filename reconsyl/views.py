from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Account


def index(request):
    account_list = Account.objects.order_by('name_text')
    context = {
        'account_list': account_list,
    }
    return render(request, 'reconsyl/index.html', context)

def account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'reconsyl/account.html', {'account': account})

def ledger(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'reconsyl/ledger.html', {'account': account})
