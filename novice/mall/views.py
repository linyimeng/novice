from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from mall.business import MallGoods,MallGoodsType,MallOrder
from urllib.parse import unquote
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from mall.forms import ShippingaddressForm
from mall.models import Shippingaddress
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
    order = MallOrder.objects.create_order(order_json,request.user,False)
    #确定地址
    addressmark = request.COOKIES.get('addresspk')
    if addressmark is None:
        address = Shippingaddress.objects.get(user=request.user,is_default=True)
    else:
        address = Shippingaddress.objects.get(pk=addressmark)
    response = render_to_response('wemall/confirm_order.html', {'order':order,'address':address})
    return response

def create_order(request):
    order_json = request.COOKIES.get('order')
    if order_json is None:
        return HttpResponse('空订单')
    else:
        order_json = unquote(order_json)
    order = MallOrder.objects.create_order(order_json,request.user,True)
    
    addressmark = request.COOKIES.get('addresspk')
    if addressmark is None:
        address = Shippingaddress.objects.get(user=request.user,is_default=True)
    else:
        address = Shippingaddress.objects.get(pk=addressmark)
    
    order = MallOrder.objects.update_address(address, order['mian'].ordercode)
    response = render_to_response("wemall/payorder.html",{"order":order})
    response.delete_cookie('order')
    response.delete_cookie('addresspk')
    return response

def view_user_center(request):
    return render(request,"wemall/user_center.html")

def view_address(request):
    is_choose=request.COOKIES.get('addressischoose')
    if is_choose == '1':
        is_choose = True
    else:
        is_choose = False
    addresses = Shippingaddress.objects.filter(user=request.user).order_by('-updated')
    print(is_choose)
    return render(request,"wemall/myaddress.html",{"addresses":addresses,'is_choose':is_choose})

def edit_address(request,address_pk):
    address = get_object_or_404(Shippingaddress,pk=address_pk)
    if request.method == "GET":
        return render(request,"wemall/myaddress_edit.html",{"address":address})
    else:
        form = ShippingaddressForm(request.POST.copy(),instance=address)
        if form.is_valid():
            address = form.save()
            return redirect("wemall/myaddress.html")
        else:
            return HttpResponse(form.errors)

def add_address(request):
    if request.method=="GET":
        return render(request,"wemall/myaddress_add.html")
    else:
        form = ShippingaddressForm(request.POST.copy())
        if form.is_valid():
            form.save()
            return redirect("wemall/myaddress.html")
        else:
            return HttpResponse(form.errors)
        
def view_order(request):
    
    return render(request,"wemall/myorder.html")

def view_mycollection(request):
    return render(request,"wemall/mycollection.html")


    

    