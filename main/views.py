from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods

# Create your views here.

from main.forms import TweetForm
from main.models import Tweet



def index(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    context={
    'tweets':tweets
    }
    return render(request, 'main/index.html', context)



@require_GET
def create_tweet_hx(request, *args, **kwargs) -> HttpResponse:
    form = TweetForm()
    context = {
        'form':form,
        'text':'Create',
    }
    return render(request, 'main/partials/_create_update_tweet.html', context)

@require_POST
def save_tweet_hxpost(request) -> HttpResponse:
    form = TweetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        tweet = form.save()
        context = {
            'tweets':tweet,
        }
    html_fragment = render_to_string('main/partials/_tweets.html', context)
    return HttpResponse(html_fragment)
