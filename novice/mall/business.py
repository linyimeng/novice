from goods.models import Goods
from django.db.models import Manager
from goods.models import Type
from order.models import Type as OrderType
from goods.models import TypeManager
from order.models import Order,Detail,OrderManager
from django.shortcuts import get_object_or_404
from json import loads
from datetime import datetime
from django.db import transaction
# Create your business here.
#         from django.db import connection
#         print(connection.queries)

def getnum(obj,gid):
    for i in obj:
        if gid == int(i['gid']):
            return int(i['num'])
    return 0

def getgids(obj):
    gids = []
    for cart in obj:
        gids.append(cart['gid'])
    return gids

class GoodsMallManager(Manager):
    '''商品业务类'''
    def get_home_goods_list(self):
        '''获取首页推荐商品列表'''
        home_goods_list = Goods.objects.filter(gsav__is_active=True)
        return home_goods_list
    
    def get_hot_goods_list(self):
        '''获取热销产品'''
        hot_goods_list = [{'name':'热销产品','goodslist':Goods.objects.filter(gsav__is_active=True)}]
        return hot_goods_list
    
    def get_goods_detail(self,gpk):
        '''获得商品详情'''
        goodsdetail = get_object_or_404(Goods,pk=gpk)
        return goodsdetail
    
    def get_cart_goods_list(self,carts_json):
        '''根据carts列表获取购物车商品信息，carts结构：[{"gid":33,"num":3},{"gid":34,"num":2}]'''
        carts = loads(carts_json)
        #提取出gid
        gids = getgids(carts)
        cartgoodss_set  = Goods.objects.filter(pk__in=gids,gsav__is_active=True)
        cartgoodss = []
        for cartgoods in cartgoodss_set:
            cg = {}
            cg['goods'] = cartgoods
            cg['num'] = getnum(carts, cartgoods.pk)
            cartgoodss.append(cg)
        return cartgoodss
    
class TypeMallManager(TypeManager):
    '''商品类型业务类'''
    def __get_category_goods_list(self,categorypk):
        '''根据分类id获取对应商品列表，默认只提取20个'''
        categoryname = Type.objects.values('pk','name').get(pk=categorypk)['name']
        goods_list = Goods.objects.filter(type__pk=categorypk)[:20]
        goodsdict=dict()
        goodsdict['name']=categoryname
        goodsdict['goodslist']=goods_list
        return goodsdict
    
    def get_root_type(self):
        '''获取无父级分类'''
        root_type = Type.objects.filter(superiors=None)
        return root_type
    
    def get_child_category_list(self,parent_pk):
        '''获取父级分类下所有子级分类及其对应分类商品的列表'''
        child_category_goods_list = []
        
        child_category_goods_list.append(self.__get_category_goods_list(parent_pk))
        
        child_categorys = Type.objects.values('pk','name').filter(superiors__pk=parent_pk)
        for child in child_categorys:
            child_category_goods_list.append(self.__get_category_goods_list(child['pk']))
        return child_category_goods_list
    
    
class MallOrderManager(OrderManager):
    '''订单业务类'''
    def create_order(self,order_json,user):
        '''根据购物车信息创建订单'''
        order = loads(order_json)
        #提取出gid
        gids = getgids(order)
        goodss = Goods.objects.filter(pk__in=gids)
        
        ordertype = OrderType.objects.get(pk=3)
        ordernum = self.__get_ordernum(user.pk,ordertype.io)
        
        totalprice = float(0)
        totalquantity = 0
        
        ordermain = Order(
                            ordercode = ordernum,
                            personal= user,
                            type = ordertype,
                            status = 'N',
                            creator = user
                        )
        #获取订单详情对象列表
        details = []
        for goods in goodss:
            num = getnum(order, goods.pk)
            detail = Detail(
                       order = ordermain,
                       goods = goods,
                       quantity = num,
                       price = goods.gsav['saleprice'],
                       gsav = goods.gsav,
                     )
            details.append(detail)
            #计算总额和总数量
            totalprice = totalprice + float(goods.gsav['saleprice'])
            totalquantity = totalquantity + int(num)
        ordermain.totalprice = totalprice
        ordermain.totalquantity = totalquantity
        with transaction.atomic():
            ordermain.save()
            Detail.objects.bulk_create(details)

        order = {'mian':ordermain,'details':details}
        return order
        
        
        
    def __get_ordernum(self,userpk,ordertype):
        ordernum = 'M' + ordertype + str(userpk) + datetime.now().strftime("%Y%m%d%H%M%S")
        return ordernum

        
    
class MallGoods(Goods):
    objects = GoodsMallManager()
    
class MallGoodsType(Type):
    objects = TypeMallManager()
    
class MallOrder(Order):
    objects = MallOrderManager()