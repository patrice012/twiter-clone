from django.urls import path
from profil import views

# app_name='profile'

urlpatterns = [
    path('<int:pk>/', views.profile, name='profile' ),
    path('', views.profile, name='profile' ),
    path('update/<int:pk>/', views.update_profile, name='update' ),
]
