from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Item
from .forms import NewItemFormPremium, EditItemFormPremium
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def multiple_filter_items(request):
    query = request.GET.get('query')
    query_two_one = request.GET.get('query_two_one')
    query_two_two = request.GET.get('query_two_two')
    query_two_three = request.GET.get('query_two_three')
    category_id = request.GET.get('category_id', 0)
    categories = Category.objects.all()
    results = Item.objects.filter(is_sold=False)

    if query_two_three:
        results = results.filter(Q(name__icontains=query_two_three) | Q(description__icontains=query_two_three))

    if query:
        results = results.filter(Q(category_id=query))

    if category_id:
        results = results.filter(Q(category_id=category_id))

    if query_two_one:
        results = results.filter(Q(name__icontains=query_two_one))

    if query_two_two:
        price_range = tuple(map(int, query_two_two.split('-')))
        results = results.filter(Q(price__range=price_range))

    items = results.filter().all()

    return render(request, 'item/multiple_filter_items.html', {
        'items': items,
        'results': results,
        'query_two_one': query_two_one if query_two_one is not None else '',
        'query_two_two': query_two_two if query_two_two is not None else '',
        'query_two_three': query_two_three if query_two_three is not None else '',
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemFormPremium(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemFormPremium()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item'
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        item.delete()
        form = EditItemFormPremium(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemFormPremium(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item'
    })

