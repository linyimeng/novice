from goods.models import Goods
from django.db.models import Manager
from goods.models import Type
from goods.models import TypeManager
from order.models import Order,Detail
from django.shortcuts import get_object_or_404
from json import loads
# Create your business here.
#         from django.db import connection
#         print(connection.queries)
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
        gids = []
        for cart in carts:
            gids.append(cart['gid'])
        cartgoodss_set  = Goods.objects.filter(pk__in=gids,gsav__is_active=True)
        cartgoodss = []
        for cartgoods in cartgoodss_set:
            cg = {}
            cg['goods'] = cartgoods
            cg['num'] = self.__getnum(carts, cartgoods.pk)
            cartgoodss.append(cg)
        print(cartgoodss)
        return cartgoodss
    def __getnum(self,carts,gid):
        for i in carts:
            if gid == int(i['gid']):
                return int(i['num'])
        return 0
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
    
    
class MallOrderManager(Manager):
    '''订单业务类'''
    def create_order(self,carts):
        '''根据购物车信息创建订单'''
        pass
    
class MallGoods(Goods):
    objects = GoodsMallManager()
    
class MallGoodsType(Type):
    objects = TypeMallManager()
    
class MallOrder(Order):
    objects = MallOrderManager()