from django.contrib.auth.decorators import login_required
from django.db.models import Q #This is use for search multiple fields 
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import *

# Create your views here.
def items(request):
    query = request.GET.get('query', '')#'' means else empty
    items = Item.objects.filter(is_sold=False)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
       items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))


    return render(request, 'items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk) #Django will give us a 404 error if this object doesn't exist in the database. Left pk(primary key) is the primary key of the model itself and right pk is the one we get from the url
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required #so without authenticate person will be redirected to the loginpage
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)#create object but not save in the database
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'form.html', {
        'form': form,
        'title': 'Create new item',
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
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit item',
    })





