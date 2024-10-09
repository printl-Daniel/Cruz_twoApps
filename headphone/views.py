from django.shortcuts import render

def index(request):
    return render(request, "headphone/index.html")
def brands(request):
    return render(request, "headphone/topbrands.html")
def specs(request):
    return render(request, "headphone/specs.html")
