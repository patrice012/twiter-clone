from django.urls import path,include
from django.contrib.auth import views as auth_views
from auth_app import views


# app_name = 'auth_app'
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.sign_in, name='register' ),

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login' ),

    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logged_out.html'), name='logged_out' ),

    # password change

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='auth/password_change_form.html'), name='password_change' ),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password_change_done' ),


    # password reset

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'), name='password_reset' ),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done' ),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm' ),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete' ),

]


# This will include the following URL patterns:
"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

"""