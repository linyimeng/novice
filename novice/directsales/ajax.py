'''
Created on 2017-1-28

@author: yimeng
'''
from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from directsales.models import Transactionhistory,Orderdetail,Order
from json import dumps
from decimal import Decimal
def test(request):
    return render(request,"directsales/500.html")

def get_awards_statistics_data(request):
    all_awards = Transactionhistory.objects.filter(track__user=request.user)
    gold = Decimaltofloat(all_awards.filter(type="gold").aggregate(Sum('price'))['price__sum'])
    integral = Decimaltofloat(all_awards.filter(type="integral").aggregate(Sum('price'))['price__sum'])
    shoppingcoupons = Decimaltofloat(all_awards.filter(type="shoppingcoupons").aggregate(Sum('price'))['price__sum'])
    total = float(gold) + float(integral) + float(shoppingcoupons)
    json = dumps({
                  "data":[
                    {
                        "label":"金币:"+gold,
                        "data":gold
                    },
                    {
                        "label":"积分:"+integral,
                        "data":integral
                    },
                    {
                        "label":"购物劵:"+shoppingcoupons,
                        "data":shoppingcoupons
                    },
                   ],
                  "total":total
                })
    return HttpResponse(json,content_type='application/json')

def Decimaltofloat(decimal):
    if isinstance(decimal, Decimal):
        return "%.2f" % decimal
    else:
        return '0';
    
def ship(request):
    pk = request.GET.get('pk')
    detail = Orderdetail.objects.get(pk=pk)
    ordernum = Orderdetail.objects.filter(ordercode=detail.ordercode).count()
    num = Orderdetail.objects.filter(ordercode=detail.ordercode,status='ship').count()
    if ordernum==num:
        return HttpResponse(dumps({'result':False}),content_type='application/json')
    elif (ordernum-num)>1:
        detail.status = "ship"
        detail.save()
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    elif (ordernum-num)==1:
        detail.status = "ship"
        detail.save()
        order = detail.ordercode
        order.status = "ship"
        order.save()
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    
@csrf_exempt
def confirmship(request):
    ordercode = request.POST.get('ordercode')
    try:
        order = Order.objects.get(ordercode=ordercode)
    except ObjectDoesNotExist:
        return HttpResponse(dumps({'result':False,'error':'订单不存在'}),content_type='application/json')
    else:
        goodsnum = Orderdetail.objects.filter(ordercode=order).count()
        num = Orderdetail.objects.filter(ordercode=order,status='ship').count()
        if goodsnum != num:
            return HttpResponse(dumps({'result':False,'error':'订单发货未完成'}),content_type='application/json')
        else:
            #发钱
            Order.objects.settlement_order(order)
            #更新订单状态
            order.status = 'end'
            order.save()
            Orderdetail.objects.filter(ordercode=order).update(status='end')
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    
    