from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import F
# Create your views here.

from main.forms import TweetForm
from main.models import Tweet




class IndexView(TemplateView):
    template_name = 'main/index.html'

index = IndexView.as_view()

# def index(request, *args, **kwargs):
#     tweets = Tweet.objects.all()
#     context={
#     'tweets':tweets
#     }
#     return render(request, 'main/index.html',context)


def load_component_hx(request):
    links = {
        'nav-bar-hx':'_navbar.html',
        'header-hx':'_header.html',
        'friends-hx':'_new_friends.html',
        # 'trends-hx':'',
        'follow-hx':'_follow.html',
    }

    for key in links.keys():
        # check if the provider url is match one in the dict
        # if true then get the relate html template
        
        if str(request.path) == f'/{key}/':
            template = links[key]
            fragment = 'main/partials/'+template
            return render(request,fragment)
    return HttpResponse(f'{request.path} is not a valid endpoint.')



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
        print(form.is_valid(), 'form.is_valid()')
        form.instance.user = request.user
        tweet = form.save()
        print(tweet.id, 'test tttttttttt')
        tweet = Tweet.objects.get(id = tweet.id)
        context = {
            'new_tweet':tweet,
        }
    html_fragment = render_to_string('main/partials/_tweets.html', context)
    return HttpResponse(html_fragment)
    # return HttpResponse('true')


class TweetListView(ListView):
    model = Tweet
    context_object_name = 'tweets'
    paginate_by = 5
    template_name ='main/partials/_tweets.html'

    def get_queryset(self):
        # keep the same order after updating an object
        return super().get_queryset().order_by('created')
    
tweet_list = TweetListView.as_view()


def tweet_actions_hx(request, *args, **kwargs) -> HttpResponse():
    pk = kwargs['id']
    print(args, kwargs)
    action_name = kwargs['name']
    if '/like/' in str(request.path):
        view_func = like_hx
    if '/views/' in str(request.path):
        view_func = tweet_views_hx
    return view_func(request, pk)


@login_required
def like_hx(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    # update the current number of like
    likes_users = tweet.users_like_id
    if request.user.id in likes_users:
        tweet.likes_by.remove(request.user)
        tweet.save()
        html = f'<span class="tooltiptext">Like</span><i class="fa-regular fa-heart"></i><h6 id="like{tweet.id}">{tweet.likes}</h6>'

    else:
        tweet.likes_by.add(request.user)
        tweet.save()
        html = f'<span class="tooltiptext">Unlike</span><i class="fa-solid fa-heart like"></i><h6 id="like{tweet.id}" class="like">{tweet.likes}</h6>'
    if request.htmx:
        return HttpResponse(html)
    return render(request, 'main/index.html')



def tweet_views_hx(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    tweet.views_by = F('views_by') + 1
    tweet.save()
    tweet.refresh_from_db()
    if request.htmx:
        html = f'<span class="tooltiptext">View</span><i class="fa fa-chart-simple"></i><h6>{tweet.view_numbers}</h6>'
        return HttpResponse(html)

    # Render the initial page with the results and the total number of pages
    context = {'tweets': page_obj, 'total_pages': total_pages}
    html_fragment = render_to_string('main/partials/_tweets_list.html',context)
    return HttpResponse(html_fragment)