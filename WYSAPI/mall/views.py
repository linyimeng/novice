from django.shortcuts import render
from mall.business import MallGoods,MallGoodsType,MallOrder
from urllib.parse import unquote
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def view_home(request):
    home_goods_list = MallGoods.objects.get_home_goods_list()
    return render(request,"wemall/home.html",{'home_goods_list':home_goods_list,})


def view_category_list(request,categorypk):
    '''商品分类展示'''
    category_list = MallGoodsType.objects.get_root_type()
    if categorypk == '888888': #888888为热销产品分类代码
        child_category = MallGoods.objects.get_hot_goods_list()
    else:
        child_category = MallGoodsType.objects.get_child_category_list(categorypk)
    return render(request,"wemall/category_list.html",{
                   'category_list':category_list,
                   'child_category':child_category,
                   'categorypk':int(categorypk),
                 })

def view_detail(request,gpk):
    goodsdetail = MallGoods.objects.get_goods_detail(gpk)
    return render(request,"wemall/goodsdetail.html",{
                   'goods':goodsdetail,
                 })

def view_carts(request):
    carts_json = request.COOKIES.get('carts')
    if carts_json is None:
        return HttpResponse('空购物车')
    else:
        carts_json = unquote(carts_json)
    cartgoodss = MallGoods.objects.get_cart_goods_list(carts_json)
    return render(request,"wemall/carts.html",{
                    'cartgoodss':cartgoodss,
                 })
    
    
#需判断是否登录
@login_required
def view_confirm_order(request):
    order_json = request.COOKIES.get('order')
    if order_json is None:
        return HttpResponse('空订单')
    else:
        order_json = unquote(order_json)
    order = MallOrder.objects.create_order(order_json,request.user)
    print(order)
    return render(request,"wemall/confirm_order.html",{'order':order})

def view_user_center(request):
    return render(request,"wemall/user_center.html")

def view_address(request):
    return render(request,"wemall/myaddress.html")

def add_address(request):
    if request.method=="GET":
        return render(request,"wemall/myaddress_add.html")
    else:
        pass
    
def view_order(request):
    return render(request,"wemall/myorder.html")

def view_mycollection(request):
    return render(request,"wemall/mycollection.html")


    

    