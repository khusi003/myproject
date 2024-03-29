"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexpage, name='home'),
    path('login-page/', views.login_page, name='loginpage'),

    path('registration/',views.registration_page, name='registration-page'),
    path('register-user/', views.register_user, name='register-page'),

    path('login-user/', views.login_user, name='login-user'),

    path('logout/',views.logout,name="logout"),

    path('forgot-password/',views.forgot_passsword,name='forgot-password'),

    path('send-otp/',views.send_otp,name='send-otp'),
    path('reset-password/',views.reset_password,name='reset-password'),
    path('profile-view/',views.profile_view,name='profile-view'),
    path('update-profile',views.update_profile,name='update-profile'),
    path('foodgallary',views.foodgallary,name='foodgallary'),
    path('upload-gallary/',views.upload_gallary,name='upload-gallary'),
    path('review/',views.review,name='review'),
    path('update-review/',views.update_review,name='update-review'),


]
