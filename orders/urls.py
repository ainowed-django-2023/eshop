from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_card)
]