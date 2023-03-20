from django.shortcuts import render, redirect
# Create your views here.



def index(request, *args, **kwargs):
    context={

    }
    return render(request, 'main/index.html', context)
