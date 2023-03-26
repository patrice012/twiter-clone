from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods

# Create your views here.

from main.forms import TweetForm
from main.models import Tweet



def index(request, *args, **kwargs):
    context={
    }
    return render(request, 'main/index.html', context)



@require_http_methods(['POST', 'GET'])
def create_tweet(request, *args, **kwargs) -> HttpResponse:
    tweet = Tweet.objects.none()
    form = TweetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet = tweet.save()

    context = {
        'form':form,
        'tweet':tweet,
    }
    return render(request, 'main/partials/_create_update_tweet.html', context)

