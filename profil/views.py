from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse, Http404, HttpResponseNotFound
# Create your views here.

from .models import Profile
from .forms import ProfileFrom

User = get_user_model()


def profile(request, *args, **kwargs):
    pk = request.user.id
    try:
        # if 'pk' in kwargs:
        #     pk = kwargs['pk']
        user = User.objects.get(id=pk)
        user_profile = user.profile
    except User.DoesNotExist:
        return HttpResponseNotFound('User not found')

    context={
    'user':user,
    'profile':user_profile,
        }
    return render(request,'profile/profile.html', context)



class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileFrom
    template_name = "profile/update.html"

update_profile = ProfileUpdateView.as_view()
