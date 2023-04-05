from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.contrib.auth.models import User
from django.db.models import Count, Q


# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })


def boutique_list(request):
    query = request.GET.get('query')
    boutiques = User.objects.all()

    if query:
        boutiques = boutiques.filter(username__icontains=query)

    boutiques = boutiques.annotate(num_items=Count('items')).filter(num_items__gte=2)

    return render(request, 'dashboard/market.html', {
        'boutiques': boutiques,
        'query': query if query is not None else '',
    })


def boutique(request, user_id):
    query = request.GET.get('query')
    user = User.objects.get(pk=user_id)
    items = Item.objects.filter(created_by=user)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'dashboard/boutique.html', {
        'items': items,
        'user': user,
        'query': query if query is not None else '',
    })


