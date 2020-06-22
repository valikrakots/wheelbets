from django.shortcuts import render
from .models import Table


def home(request):
    context = {
        'posts': list(Table.objects.order_by('-date')),
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


def help(request):
    return render(request, 'blog/help.html', {'title': 'help'})


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'contacts'})
