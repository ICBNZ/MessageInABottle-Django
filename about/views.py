from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def game(request):
    return render(request, 'game.html')

def privacy(request):
    return render(request, 'privacy.html')

def something_fishy(request):
    return render(request, 'something_fishy.html')
