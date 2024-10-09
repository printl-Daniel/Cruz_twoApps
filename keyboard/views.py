from django.shortcuts import render

def index(request):
    return render(request, "keyboard/index.html")
def shortcut(request):
    return render(request, "keyboard/shortcut.html")
def specs(request):
    return render(request, "keyboard/specs.html")
