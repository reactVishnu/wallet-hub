from django.urls import path
from .views import login_view, success_view, home_view, signup_view

app_name = 'operations'

urlpatterns = [path('login',login_view, name='login'),
               path('', home_view, name='home'),
               path('success', success_view, name='success'),
               path('signup', signup_view, name='signup'),
               ]
