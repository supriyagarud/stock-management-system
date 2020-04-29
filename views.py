from django.shortcuts import render

# Create your views here.
from storemgmt.forms import StockCreateForm
from storemgmt.models import Stock
from django.shortcuts import render, redirect


def home(request):
    title = 'Welcome: This is the Home Page'
    form = 'Welcome: This is the Home Page'
    context = {
        "title": title,
        "text": form,
    }
    return render(request, "home.html", context)


def list_item(request):
    title = "List of items"
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)
