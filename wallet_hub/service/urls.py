from django.urls import path
from .views import basic_text_details

app_name = 'service'

urlpatterns = [path('welcome', basic_text_details, name='login')]
