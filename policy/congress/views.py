from django.shortcuts import render

def index(request, template='congress/index.html'):
    return render(request, template)
