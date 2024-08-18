from django.urls import path
from homespace.views.home import *

urlpatterns = [
    path('', home, name='home')
]