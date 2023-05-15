from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Order

def index(request):
    return render(request, 'orders/index.html', {
        'page_title': 'Orders',
        'app': 'index',
        'page': 'orders',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def ajax_card(request):
    response = dict()
    response['test_message'] = 'AJAX works fine!'

    uid = request.GET.get('uid')
    pid = request.GET.get('pid')

    Order.objects.create(
        code=f'Order-{pid}/{uid}/{timezone.now()}',
        user_id=uid,
        products_id=pid,
        notes='Waiting for confirmation'
    )

    total = 0
    user_orders = Order.objects.filter(user_id=uid)
    for order in user_orders:
        total += order.products.price * order.count

    response['count'] = len(user_orders)
    response['total'] = total

    return JsonResponse(response)