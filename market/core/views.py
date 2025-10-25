from django.shortcuts import render,redirect
from item.models import Category, Item
from core.models import Review
from .forms import SignupForm, FeedbackForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:8] #because we don't want product that is sold
    categories = Category.objects.all()
    reviews = Review.objects.filter(is_viewed=True)

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
        'reviews': reviews,
    })

def review(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    form = FeedbackForm()
    context = {'form': form}
    return render(request, 'review.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {
        'form': form
    })








