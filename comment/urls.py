from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.comment_detail_hx, name="comment_detail"),
    # path('', views.all_comments, name="all_comments"),
]
