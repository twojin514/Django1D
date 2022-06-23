from django.shortcuts import render

def first(request):
    return render(request,'first.html')

def secound(request):
    return render(request,'secound.html')

def th(request):
    return render(request,'third.html')