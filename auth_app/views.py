from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import RegisterForm

# Create your views here.

User = get_user_model()

def sign_in(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect(reverse('login'))
    context ={
    'form':form
    }
    return render(request, 'auth/register.html', context)