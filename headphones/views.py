from django.shortcuts import render

def index(request):
    return render(request, "headphones/index.html")
def brands(request):
    return render(request, "headphones/topbrands.html")
def specs(request):
    return render(request, "headphones/specs.html")
