from django.urls import path, include
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/', views.tweet_list, name='tweet_list')
]

htmx_urlpatterns = [
    path('creat-tweet/', views.create_tweet_hx, name='create_tweet_hx'),
    path('save-tweet/', views.save_tweet_hxpost, name='save_tweet_hxpost'),
    # path('like/<int:tweet_id>/', views.like_hx, name='like_hx'),
    path('actions/<str:name>/<int:id>/', views.tweet_actions_hx, name='tweet_actions_hx'),


    path('nav-bar-hx/', views.load_component_hx, name='load_nav_bar_hx'),
    path('header-hx/', views.load_component_hx, name='load_header_hx'),
    path('friends-hx/', views.load_component_hx, name='load_friends_hx'),
    # path('trends-hx/', views.load_component_hx, name='load_trends_hx'),
    path('follow-hx/', views.load_component_hx, name='load_follow_hx'),
]

urlpatterns += htmx_urlpatterns
