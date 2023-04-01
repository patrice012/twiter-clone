from django.urls import reverse


def lazy_loading_links(request):
    nav_bar_link = reverse('load_nav_bar_hx')
    load_header_hx = reverse('load_header_hx')
    load_friends_hx = reverse('load_friends_hx')
    load_trends_hx = reverse('load_trends_hx')
    load_follow_hx = reverse('load_follow_hx')

    context_link = {
        'nav_bar_link': nav_bar_link,
        'load_header_hx':load_header_hx,
        'load_friends_hx':load_friends_hx,
        'load_trends_hx':load_trends_hx,
        'load_follow_hx':load_follow_hx,
    }

    return context_link