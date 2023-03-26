from django.urls import path, include


from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/', views.create_tweet, name='create_tweet'),
]
