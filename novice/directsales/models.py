from django.db import models
from django.db.models import Manager
from django.db.models import Count,Sum
from django.db import connection
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from json import loads
from datetime import datetime
from mall.models import Shippingaddress
# Create your models here.

def init_bonus(track,user):
    if not isinstance(track, Doubletrack):
        try:
            track = Doubletrack.objects.get(pk=track)
        except ObjectDoesNotExist:
            raise ValueError('参数错误')
    bonus = Bonus.objects.create(track=track,updater=user,gold=0,shoppingcoupons=0,integral=0)
    th = Transactionhistory.objects.filter(track=track).aggregate(Sum('price'))
    Transactionhistory.objects.filter(track=track).update(is_bonus=True)
    bonus.gold=th.price_sum
    bonus.save()
    return bonus
    
    

class DoubletrackManager(Manager):
    def get_member_info(self,track,parent=None,isright=None):
        if track=="":
            track_root = Doubletrack.objects.get(parent=parent,isright=isright)
            pk = track_root.pk
        else:
            pk = track.pk
        query = '''
                select track.id as id,track.user_id as user_id, track.name as name, 
                track.identity_id as identity_id,track.parent_id as parent_id,track.joined as joined,
                (select get_node_child_count_recursion(track.id,false) ) as left_num,
                (select get_node_child_count_recursion(track.id,true)) as right_num
                from directsales_doubletrack track
                where track.id = %s;
        '''
        track_info = Doubletrack.objects.raw(query,[pk])
        return track_info
      
    def checking_doubletrack(self,user):
        '''检查2个节点'''
        parentcount = Doubletrack.objects.filter(parent__user__pk=user.pk).count()
        if parentcount>=2:
            return False
        else:
            return True
        
    def checking_istrack(self,username):
        '''检查是否是节点用户'''
        try:
            user = User.objects.get(username=username)
            Doubletrack.objects.get(user=user)
        except ObjectDoesNotExist:
            return False
        else:
            return True
    
    def get_track_child_list(self,track):
        '''获取当前节点的所有子节点列表'''
        query = '''
        WITH RECURSIVE child
        AS (
             SELECT id,user_id,identity_id,joined,updated,parent_id,directpushuser_id,isright
             FROM directsales_doubletrack 
             WHERE id=%s
             UNION ALL
             SELECT dd.id,dd.user_id,dd.identity_id,dd.joined,dd.updated,dd.parent_id,dd.directpushuser_id,dd.isright
             FROM directsales_doubletrack AS dd 
             INNER JOIN child 
             ON child.id = dd.parent_id
           )
        SELECT id,user_id,identity_id,parent_id,directpushuser_id,joined,updated,
            (SELECT count(*) FROM child as ch WHERE ch.directpushuser_id=child.id and ch.id<>child.id) AS directpushcount,
            get_node_child_count_recursion(id,true) AS rightcount,
            get_node_child_count_recursion(id,false) AS leftcount
        FROM child
        WHERE id<>%s
        order by joined;
        '''
        child_list = Doubletrack.objects.raw(query,[track.pk,track.pk])
        return child_list
    

class Doubletrack(models.Model):
    user = models.OneToOneField(User,verbose_name = '用户名')
    parent = models.ForeignKey('self',blank=True,null=True,verbose_name="父节点")
    isright= models.BooleanField(blank=True,default=True,verbose_name="是否右")
    identity = models.ForeignKey('Memberlevel',verbose_name="会员等级")
    is_active = models.BooleanField(default=True)
    
    directpushuser = models.ForeignKey('self',blank=True,null=True,related_name='directpush',verbose_name="直推人")
    name = models.CharField('名字',max_length=10)
    phone= models.CharField('手机',max_length=20)
    address = models.TextField('地址',blank=True,null=True)
    bank = models.CharField('开户银行',max_length=30)
    bank_account = models.CharField('银行帐号',max_length=30)
    pay_password = models.CharField(max_length=30)
    
    depth = models.IntegerField(blank=True,null=True)
    path = models.CharField(max_length=300,blank=True,null=True)
    priority = models.IntegerField('权重',blank=True,null=True)
    directpush_path = models.CharField(max_length=300,blank=True,null=True)
    joined = models.DateTimeField(_('创建时间'),auto_now_add=True)
    updated = models.DateTimeField(_('更新时间'),auto_now=True)
    creator = models.ForeignKey(User,blank=True,null=True,related_name='creator_doubletrack',verbose_name="创建人")

    objects= DoubletrackManager()
    
    class Meta:
        verbose_name = '节点信息'
        verbose_name_plural = '节点信息'
        
    def __str__(self):
        return self.user.username
        
    def save(self, *args, **kwargs):
        if self.parent is not None:
            parent = Doubletrack.objects.filter(parent=self.parent)
            if self.pk is None:
                #如果是新增时，确保每个用户下有只有2个用户
                count = parent.count()
                if count >= 2:
                    raise ValueError('parent Can not exceed two')
                #确保左右两分支
                if count!=0:
                    if parent[0].isright is self.isright:
                        self.isright = not self.isright
        super(Doubletrack,self).save(*args, **kwargs)
        
    
        
class Bonus(models.Model):
    track = models.OneToOneField(Doubletrack,verbose_name="节点名称")
    gold = models.DecimalField('金币余额',max_digits=10,decimal_places=2,blank=True,null=True)
    integral = models.IntegerField('积分余额',blank=True,null=True)
    shoppingcoupons = models.DecimalField('购物劵余额',max_digits=10,decimal_places=2,blank=True,null=True)
    freeze_gold = models.DecimalField('冻结账户余额',max_digits=10,decimal_places=2,blank=True,null=True)
    
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('最后一次修改时间'),auto_now=True)
    updater = models.ForeignKey(User,verbose_name="修改人")
    
    def __str__(self):
        return self.track.name
    
    class Meta:
        verbose_name = '用户账户统计'
        verbose_name_plural = '用户账户统计'

class Memberlevel(models.Model):
    '''成员等级'''
    name = models.CharField('等级名称',max_length=30)
    price=models.DecimalField('价格',max_digits=18,decimal_places=8)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "会员等级"
        verbose_name_plural = "会员等级"
    
class TransactionhistoryManager(Manager):
    def registered_deduct_gold(self,identity_id,user,reguser):
        '''注册用户时扣除金币,并记录交易信息，更新bonus表,并生成奖金信息保存'''
        track = Doubletrack.objects.get(user = user)
        bonus = Bonus.objects.get(track=track)
        member = Memberlevel.objects.get(pk=identity_id)
        gold = bonus.gold
        deduct_gold = member.price
        if gold >= deduct_gold:
            remark = '注册' + member.name + '会员,扣除金币:' + str("%.2f"%deduct_gold)
            Transactionhistory.objects.create(track=track,memberlevel=member.name,
                                              type='gold',price=deduct_gold,io='O',
                                              pay_by='gold',remark=remark,is_bonus=True,is_active=True)
            
            #计算奖金
            track = Doubletrack.objects.get(user=reguser)
            cursor = connection.cursor()
            cursor.execute('select awards(%s,%s);',[track.pk,deduct_gold])
        else:
            raise ValueError('错误的时机调用')
    
        
    def upgrade_deduct_gold(self,upgrade_identity_id,user):
        '''升级用户时扣除金币，并记录交易信息，更新bonus表'''
        track = Doubletrack.objects.get(user = user)
        bonus = Bonus.objects.get(track=track)
        oldmember = track.identity
        newmember = Memberlevel.objects.get(pk=upgrade_identity_id)
        gold = bonus.gold
        deduct_gold = newmember.price - oldmember.price
        if gold > deduct_gold:
            remark = '升级' + oldmember.name + '为'+ newmember.name + '会员,扣除金币:' + str("%.2f"%deduct_gold)
            Transactionhistory.objects.create(track=track,memberlevel=oldmember.name,
                                              type='gold',price=deduct_gold,io='O',
                                              pay_by='gold',remark=remark,is_bonus=True,is_active=True)
            track.identity = newmember
            track.save()
        else:
            raise ValueError('错误的时机调用')
    
    def isenough(self,transfer_type,track,price):
        try:
            bonus = Bonus.objects.get(track=track)
        except:
            raise ValueError('user is does not exist')
        else:
            overage = getattr(bonus,transfer_type,0)
            print(overage)
            print(price)
            if price > overage:
                raise ValueError('账户余额不足')
            else:
                return True
    
    def transfer(self, accept, pricenumstr, senduser, transfer_type):
        #判断接收者是否存在，并获取接收者节点信息
        pricenum = float(pricenumstr)
        try:
            accept_user = User.objects.get(username=accept)
            accept_track = Doubletrack.objects.get(user=accept_user)
        except ObjectDoesNotExist:
            raise ValueError('accept user is does not exist!')
        else:
            #判断senduser金币是否足够
            send_track = Doubletrack.objects.get(user=senduser)
            self.isenough(transfer_type, send_track, pricenum)
            ##扣除发送用户金币,并生成交易记录
            
            #确定中文
            if transfer_type=="gold":
                transfer_type_name = '金币'
            elif transfer_type == "integral":
                transfer_type_name = "积分"
            else:
                transfer_type_name='购物劵'
            
            
            remark = "转账至" + accept + ",扣除"+ transfer_type_name +":" + str("%.2f"%pricenum)
            Transactionhistory.objects.create(track=send_track,memberlevel=send_track.identity.name,
                                              type=transfer_type,price=pricenum,io='O',
                                              pay_by=transfer_type,remark=remark,is_bonus=True,is_active=True)
            
            ##增加接收用户金币，并生成交易记录
            remark = "接收"+senduser.username + transfer_type_name +"转账,增加"+ transfer_type_name+":" + str("%.2f"%pricenum)
            Transactionhistory.objects.create(track=accept_track,memberlevel=accept_track.identity.name,
                                              type=transfer_type,price=pricenum,io='I',
                                              pay_by=transfer_type,remark=remark,is_bonus=True,is_active=True)
    
    def withdraw(self,user,bank,bank_account,goldstr):
        gold = float(goldstr)
        track = Doubletrack.objects.get(user=user)
        bonus = Bonus.objects.get(track=track)
        if bonus.gold < gold:
            raise ValueError('账户金币不足')
        else:
            remark = '用户提现'+str("%.2f"%gold)+'至' + bank + ':' + bank_account
            th = Transactionhistory.objects.create(track=track,memberlevel=track.identity.name,
                                              type='gold',price=gold,io="O",
                                              pay_by='gold',remark=remark,is_bonus=True,is_active=True)
            
            #计算提现税额和提现手续
            from directsales.settings import TAX_RATE,WITHDRAWAL_FEE
            tax = gold * TAX_RATE
            fee = gold * WITHDRAWAL_FEE
            real_price = gold - (tax + fee)
            wh = Withdrawhistory.objects.create(user=user,transaction_related=th,bank=bank,bank_account=bank_account,tax=tax,
                                           fee=fee,price=gold,real_price=real_price,into_account=False,is_active=True)
            return wh
    
    def get_notification(self,user):
        track = Doubletrack.objects.get(user=user)
        thn = Transactionhistory.objects.filter(track=track,notification=False).values('type').annotate(rawnum=Count('*'))
        return thn
        
class Transactionhistory(models.Model):
    '''交易记录'''
    PAY_BY = (
        ('cash','现金'),
        ('cup','银联'),
        ('alipay','支付宝'),
        ('wechatpayment','微信支付'),
        ('system','系统发放'),
        ('gold','账户金币'),
        ('integral','账户积分'),
        ('shoppingcoupons','账户购物劵'),
    )
    TRANSACTION_TYPE = (
        ('gold','金币'),
        ('integral','积分'),
        ('shoppingcoupons','购物劵'),
    )
    IO = (
        ('I','增加'),
        ('O','减少'),
    )
    track = models.ForeignKey(Doubletrack)
    memberlevel = models.CharField('会员等级',max_length=30)
    type = models.CharField('货币类型',max_length=20,choices=TRANSACTION_TYPE)
    price= models.DecimalField('金额',max_digits=18,decimal_places=8)
    io = models.CharField('进出',max_length=1,choices=IO)
    overage = models.DecimalField('当时余额',max_digits=18,decimal_places=8,blank=True,null=True)
    pay_by=models.CharField('支付方式',max_length=30,choices=PAY_BY)
    event = models.CharField('暂无用',max_length=30,blank=True,null=True)
    event_type = models.CharField('暂无用',max_length=30,blank=True,null=True)
    remark=models.TextField('备注',blank=True,null=True)
    notification = models.NullBooleanField('是否通知',default=False,blank=True,null=True)
    is_active = models.BooleanField('是否冻结',default=True)
    is_bonus = models.NullBooleanField('是否计算入账户',default=False,blank=True,null=True)
    source_track = models.IntegerField('交易引发源',blank=True,null=True)
    joined = models.DateTimeField(_('时间'),auto_now_add=True)
    objects = TransactionhistoryManager()
    def __str__(self):
        return self.track.name
    class Meta:
        verbose_name = "交易记录"
        verbose_name_plural = "交易记录"
    
class Awards(models.Model):
    name = models.CharField('奖金名称',max_length=30)
    keyword=models.CharField('程序关键词',max_length=20)
    memberlevel = models.ForeignKey(Memberlevel,verbose_name="会员等级")
    percentage = models.DecimalField('提成比例',max_digits=4,decimal_places=3)
    seniority_num = models.IntegerField('代数',blank=True,null=True)
    layer_num = models.IntegerField('层数',blank=True,null=True)
    
    def __str__(self):
        return self.keyword
    class Meta:
        verbose_name = "奖金类型"
        verbose_name_plural = "奖金类型"
    
class nodehistory(models.Model):
    node = models.ForeignKey(Doubletrack,related_name='track')
    follow = models.ForeignKey(Doubletrack,blank=True,null=True,related_name='withid')
    depth = models.IntegerField()
    type = models.CharField(max_length=30)
    awards=models.DecimalField(max_digits=18,decimal_places=8)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    
class Withdrawhistory(models.Model):
    '''申请'''
    user = models.ForeignKey(User)
    transaction_related = models.OneToOneField(Transactionhistory)
    bank = models.CharField('银行',max_length=60)
    bank_account = models.CharField('银行账户',max_length=30)
    tax = models.DecimalField('税额',max_digits=18,decimal_places=8)
    fee = models.DecimalField('手续费',max_digits=18,decimal_places=8)
    price= models.DecimalField('提现金额',max_digits=18,decimal_places=8)
    real_price = models.DecimalField('到帐金额',max_digits=18,decimal_places=8)
    into_account = models.NullBooleanField('是否到帐',default=False,blank=True,null=True)
    remark = models.TextField('备注',blank=True,null=True)
    joined = models.DateTimeField(_('申请时间'),auto_now_add=True)
    updated = models.DateTimeField(_('到帐时间'),auto_now=True)
    
    class Meta:
        verbose_name = "提现申请记录"
        verbose_name_plural = "提现申请记录"
    
class Super_total(models.Model):
    into = models.DecimalField(max_digits=18,decimal_places=8)
    tout = models.DecimalField(max_digits=18,decimal_places=8)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    
class Bulletin_board(models.Model):
    '''公告栏'''
    title = models.CharField(max_length=30)
    content = models.TextField()
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    
class Events_priority(models.Model):
    event_name = models.CharField(max_length=30)
    priority = models.IntegerField()
    
class Goods(models.Model):
    name = models.CharField('商品名称',max_length=60)
    image = models.ImageField(upload_to="directsale_images")
    supplier = models.ForeignKey(Doubletrack,verbose_name="'供应商")
    description = models.CharField('商品介绍',max_length=120,blank=True,null=True)
    price = models.DecimalField('价格',max_digits=18,decimal_places=8)
    integral = models.DecimalField('积分价',max_digits=18,decimal_places=8)
    shoppingcoupons = models.DecimalField('购物劵',max_digits=18,decimal_places=8)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

class OrderManager(Manager):
    def create_order(self,pay_by,addresspk,jsonstr,user):
        goodsdetail = loads(jsonstr)
        bonus = Bonus.objects.get(track__user=user)
#       创建订单
        ordercode = str(user.pk) + datetime.now().strftime('%Y%m%d%H%M%S')
        if addresspk=="0":
            address = Shippingaddress.objects.create(recipient=bonus.track.name,mobile=bonus.track.phone,address=bonus.track.address,user=user)
        else:
            address = Shippingaddress.objects.get(pk=addresspk)
        remark = "购买商品，订单号：" + ordercode
        order = Order.objects.create(user=user,ordercode=ordercode,pay_by=pay_by,totalprice=0,totalquantity=0,
                                     ship_recipient=address.recipient,ship_mobile=address.mobile,ship_address=address.address,status='pay')
        totalprice = 0
        totalquantity = 0
        for gd in goodsdetail:
            if gd['quantity']!='0':
                try:
                    goods = Goods.objects.get(pk=gd['gpk'])
                except ObjectDoesNotExist:
                    raise ValueError('gpk does not exist')
                else:
                    detail = Orderdetail.objects.create(supplier=goods.supplier,ordercode=order,goodsname=goods.name,
                                                        price=goods.price,quantity=gd['quantity'],status='pay')
                    totalprice = totalprice + (detail.price * int(detail.quantity))
                    totalquantity = totalquantity + int(detail.quantity)
        
        if pay_by == "gold":
            if totalprice > bonus.gold:
                raise ValueError('金币不足')
        elif pay_by=="integral":
            if totalprice > bonus.integral:
                raise ValueError('积分不足')
        else:
            if totalprice > bonus.shoppingcoupons:
                raise ValueError('购物劵不足')
        order.totalprice = totalprice
        order.totalquantity = totalquantity
        order.save()
        Transactionhistory.objects.create(track=bonus.track,memberlevel=bonus.track.identity.name,
                                              type=pay_by,price=totalprice,io="O",
                                              pay_by=pay_by,remark=remark,is_bonus=True,is_active=True)
         
        return ordercode

        


class Order(models.Model):
    ORDER_STATUS = (
        ('pay','已付款'),
        ('ship','已发货'),
        ('end','已收货'),                
    )
    user = models.ForeignKey(User,related_name="directsale_order_user")
    ordercode = models.CharField(max_length=20)
    pay_by = models.CharField(max_length=20,choices=Transactionhistory.PAY_BY)
    
    totalquantity = models.IntegerField('商品数量')
    totalprice = models.DecimalField('总金额',max_digits=18,decimal_places=8)
    
    status = models.CharField('订单状态',max_length=30,choices=ORDER_STATUS)
    ship_recipient = models.CharField('收货人',max_length=30)
    ship_mobile = models.CharField('联系方式',max_length=20)
    ship_address = models.CharField('收货地址',max_length=300)
    
    joined = models.DateTimeField('订单时间',auto_now_add=True)
    updated = models.DateTimeField('更新时间',auto_now=True)
    
    objects = OrderManager()
    def __str__(self):
        return self.ordercode
    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
    
class Orderdetail(models.Model):
    ordercode = models.ForeignKey(Order,verbose_name="订单号")
#     goods = models.ForeignKey(Goods)
    goodsname = models.CharField('商品名称',max_length=60)
    supplier = models.ForeignKey(Doubletrack,verbose_name="'供应商")
    price = models.DecimalField('价格',max_digits=18,decimal_places=8)
    quantity = models.IntegerField('数量')
    status = models.CharField('订单状态',max_length=30,choices=Order.ORDER_STATUS)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"
    