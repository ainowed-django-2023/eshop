from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Order
from django.core.mail import send_mail

def index(request):
    return render(request, 'orders/index.html', {
        'page_title': 'Orders',
        'app': 'index',
        'page': 'orders',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })

def bill(request, sel_list: str):
    sel_list_str = sel_list.split(',')
    sel_list_num = [int(x) for x in sel_list_str[:-1]]
    total_price = int(sel_list_str[-1])
    final_list = []
    #
    for order_id in sel_list_num:
        order = Order.objects.get(id=order_id)
        final_list.append({
            'product_name': order.products.name,
            'category_name': order.products.category.name,
            'product_price': order.products.price,
            'product_photo': order.products.photo
        })

    return render(request, 'orders/bill.html', {
        'title': 'Оформлення',
        'page': 'bill',
        'app': 'orders',
        'total_price': total_price,
        'final_list': final_list,
        'init_list': sel_list
    })


def confirm(request, init_list: str):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', {
            'page_title': 'Confirm',
            'app': 'index',
            'page': 'confirm',
            'user_orders': Order.objects.filter(user_id=request.user.id),
            'init_list': init_list
        })
    elif request.method == 'POST':
        email = request.POST.get('email')

        sel_list_str = init_list.split(',')
        sel_list_num = [int(x) for x in sel_list_str[:-1]]
        total_price = int(sel_list_str[-1])
        final_list = []
        #
        for order_id in sel_list_num:
            order = Order.objects.get(id=order_id)
            final_list.append({
                'product_name': order.products.name,
                'category_name': order.products.category.name,
                'product_price': order.products.price,
            })
        #
        subject = 'Повідомлення про замовлення на сайті E-Shop'
        body = """
            <h1>Повідомлення про замовлення на сайті E-Shop</h1>
            <hr/>
            <h2 style="color: purple">Ви підтвердили замовлення настопних товарів: </h2>
            <h3>
            <ol>
        """
        for item in final_list:
            body += f"""
                <li>{item['product_name']} / {item['category_name']} - {item['product_price']} uah.</li>
            """
        body += f"""
            </ol>
            </h3>
            <hr />
            <h2>Загальна сума до сплати: <span style="color: red">{total_price} uah</span></h2>
        """
        #
        success = send_mail(subject, '', 'eshop@gmail.com', [email], fail_silently=False, html_message=body)

        if success:
            return render(request, 'orders/thanks.html', {
                'page_title': 'Подяка за замовлення',
                'app': 'thanks',
                'page': 'orders',
            })
        else:
            return render(request, 'orders/failed.html', {
                'page_title': 'Помилка поштового відправлення',
                'app': 'failed',
                'page': 'orders',
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

def ajax_cart_display(request):
    response = dict()
    uid = request.GET.get('uid')
    user_orders = Order.objects.filter(user_id=uid)

    total = 0
    for order in user_orders:
        total += order.products.price * order.count

    response['count'] = len(user_orders)
    response['total'] = total

    return JsonResponse(response)

def ajax_order_del(request):
    response = dict()

    ItemId = request.GET.get('productId')
    product_del = Order.objects.get(id=ItemId)
    product_del.delete()

    response['result'] = 'Запит для співробітника був видалений'

    return JsonResponse(response)
