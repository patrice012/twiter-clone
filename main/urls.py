from django.urls import path, include
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/', views.tweet_list, name='tweet_list')
]

htmx_urlpatterns = [
    path('creat-tweet/', views.create_tweet_hx, name='create_tweet_hx'),
    path('save-tweet/', views.save_tweet_hxpost, name='save_tweet_hxpost'),
]

urlpatterns += htmx_urlpatterns
