from django.shortcuts import render


def index(request):
    """ renders the home page """
    return render(request, 'home/index.html')