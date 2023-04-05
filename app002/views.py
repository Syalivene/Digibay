from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout


# Create your views here.
def index(request):
    query = request.GET.get('query')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'app002/index.html', {
        'categories': categories,
        'items': items,
        'query': query if query is not None else '',
    })


def contact(request):
    return render(request, 'app002/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'app002/signup.html', {
        'form': form
    })


def my_logout(request):
    logout(request)
    return redirect('app002:index')


def home_items(request):
    query = request.GET.get('query')
    items = Item.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'dashboard/boutique.html', {
        'items': items,
        'query': query,
    })
