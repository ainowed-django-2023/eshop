from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_card),
    path('ajax_cart_display', ajax_cart_display)
]