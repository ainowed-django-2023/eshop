from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_card),
    path('ajax_cart_display', ajax_cart_display),
    path('ajax_order_del', ajax_order_del),
    re_path(r'^bill/(?P<sel_list>[0-9\,]{3,})$', bill),
    re_path(r'^confirm/(?P<init_list>[0-9\,]{3,})$', confirm)
]