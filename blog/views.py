from django.shortcuts import render
from .models import Table
from django.utils import timezone


def home(request):
    context = {
        'posts': list(Table.objects.order_by('-date')),
        'postw': Table.objects.all().last(),
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


def help(request):
    return render(request, 'blog/help.html', {'title': 'help'})


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'contacts'})


def where(request):
    return render(request, 'blog/where.html', {'title': 'where'})
