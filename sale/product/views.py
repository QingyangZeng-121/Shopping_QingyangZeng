import math
from django.shortcuts import render, redirect
from product.models import ProductBrand, Product, Order
from user.models import User
from django.http.response import JsonResponse
import datetime
import time
import random


# Create your views here.
def index(request):
    if request.method == 'GET':
        if request.session.get('username'):
            userinfo = {
                "islogin": 1,
                "username": request.session['username']
            }
        else:
            userinfo = {
                "islogin": 0
            }
        search_val = request.GET.get('search_val', '')
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
        limit = 20
        if search_val:
            product = Product.objects.filter(title__contains=search_val)
            total = product.count()
            product = product.all()[(page - 1) * limit:page * limit]
        else:
            product = Product.objects.filter()
            total = product.count()
            product = product.all()[(page - 1) * limit:page * limit]
        total_pages = math.ceil(total / limit)

        return render(request, 'index.html', {"userinfo": userinfo,
                                              "product": product,
                                              "search_val": search_val,
                                              "total_pages": total_pages,
                                              "page": page})
    return render(request, 'index.html')


def statistics(request):
    return render(request, 'statistics.html')

def area(request):
    return render(request, 'area.html')


def detail(request):
    _id=request.GET.get('id')
    product = Product.objects.filter(id=_id).first()
    price=product.price
    return render(request, 'detail.html',{
        "product":product,
        "price":price
    })


def purchase(request):
    if request.method == 'GET':
        if not request.session.get('username'):
            return JsonResponse({"status": 10001, "msg": 'please log in first'})
        product_id = request.GET.get('id')
        product_count = int(request.GET.get('product_count', 1))
        product = Product.objects.filter(id=product_id).first()
        if product.inventory < product_count:
            return JsonResponse({"status": 10001, "msg": 'Insufficient inventory'})
        order_id = str(datetime.datetime.fromtimestamp(time.time())).replace("-", "").replace(" ", "").replace(":",
                                                                                                               "").replace(
            ".", "") + str(random.randint(100, 999))
        order = Order()
        order.order_num = order_id
        order.image = product.image
        user = User.objects.filter(user_name=request.session.get('username')).first()
        order.user = user
        order.title = product.title
        order.status = 'ordered'
        order.total_price = product.price * product_count
        order.number = product_count
        order.save()
        return JsonResponse({"status": 10000, "msg": 'Purchase successful'})


def cancellation(request):
    if request.method == 'GET':
        order_id = request.GET.get('id')
        order = Order.objects.filter(id=order_id).first()
        if not order:
            return render(request, 'order.html', {})
        order.status = 'canceled'
        order.save()
        if request.session.get('username'):
            userinfo = {
                "islogin": 1,
                "username": request.session['username']
            }
        else:
            userinfo = {
                "islogin": 0
            }

        user = User.objects.filter(user_name=request.session.get('username')).first()

        orders = Order.objects.filter(user=user).all()

        return render(request, 'order.html', {"userinfo": userinfo,
                                              "orders": orders})


def order(request):
    if request.method == 'GET':
        if request.session.get('username'):
            userinfo = {
                "islogin": 1,
                "username": request.session['username']
            }
        else:
            userinfo = {
                "islogin": 0
            }
        user = User.objects.filter(user_name=request.session.get('username')).first()

        orders = Order.objects.filter(user=user).all()

        return render(request, 'order.html', {"userinfo": userinfo,
                                              "orders": orders})
