
from django.db import models
from django.db.models import Manager
from django.db.models import F,Count,Sum
from django.db import connection
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
# Create your models here.

def init_bonus(track,user):
    if not isinstance(track, Doubletrack):
        try:
            track = Doubletrack.objects.get(pk=track)
        except ObjectDoesNotExist:
            raise ValueError('参数错误')
    bonus = Bonus.objects.create(track=track,updater=user,cash=0,shoppingcoupons=0,integral=0)
    th = Transactionhistory.objects.filter(track=track).aggregate(Sum('price'))
    Transactionhistory.objects.filter(track=track).update(is_bonus=True)
    bonus.cash=th.price_sum
    bonus.save()
    return bonus
    
    

class DoubletrackManager(Manager):
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
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self',blank=True,null=True)
    isright= models.BooleanField(blank=True,default=True)
    identity = models.ForeignKey('Memberlevel')
    
    directpushuser = models.ForeignKey('self',blank=True,null=True,related_name='directpush')
    name = models.CharField(max_length=10)
    phone= models.CharField(max_length=20)
    address = models.TextField(blank=True,null=True)
    bank = models.CharField(max_length=30)
    bank_account = models.CharField(max_length=30)
    pay_password = models.CharField(max_length=30)
    
    depth = models.IntegerField(blank=True,null=True)
    path = models.CharField(max_length=300,blank=True,null=True)
    priority = models.IntegerField(blank=True,null=True)
    directpush_path = models.CharField(max_length=300,blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)

    objects= DoubletrackManager()
    
    def __str__(self):
        return self.user.username
    def clean_isright(self):
        print(self.isright)
        
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
    track = models.OneToOneField(Doubletrack)
    cash = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    integral = models.IntegerField(blank=True,null=True)
    shoppingcoupons = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    updater = models.ForeignKey(User)
    
    def __str__(self):
        return self.track.name

class Memberlevel(models.Model):
    '''成员等级'''
    name = models.CharField(max_length=30)
    price=models.DecimalField(max_digits=18,decimal_places=8)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    def __str__(self):
        return self.name
    
class TransactionhistoryManager(Manager):
    def registered_deduct_cash(self,identity_id,user,reguser):
        '''注册用户时扣除金币,并记录交易信息，更新bonus表,并生成奖金信息保存'''
        track = Doubletrack.objects.get(user = user)
        bonus = Bonus.objects.get(track=track)
        member = Memberlevel.objects.get(pk=identity_id)
        cash = bonus.cash
        deduct_cash = member.price
        if cash >= deduct_cash:
            newcash = cash - deduct_cash
            bonus.cash = newcash
            remark = '注册' + member.name + '会员,扣除金币:' + str(deduct_cash)
            Transactionhistory.objects.create(track=track,memberlevel=member.name,
                                              type='gold',price=deduct_cash,io='O',
                                              overage=cash,pay_by='gold',remark=remark,is_bonus=True)
            bonus.save()
            
            #计算奖金
            track = Doubletrack.objects.get(user=reguser)
            cursor = connection.cursor()
            cursor.execute('select awards(%s,%s);',[track.pk,deduct_cash])
        else:
            raise ValueError('错误的时机调用')
    
        
    def upgrade_deduct_cash(self,upgrade_identity_id,user):
        '''升级用户时扣除金币，并记录交易信息，更新bonus表'''
        track = Doubletrack.objects.get(user = user)
        bonus = Bonus.objects.get(track=track)
        oldmember = track.identity
        newmember = Memberlevel.objects.get(pk=upgrade_identity_id)
        cash = bonus.cash
        deduct_cash = newmember.price - oldmember.price
        if cash > deduct_cash:
            newcash = cash - deduct_cash
            bonus.cash = newcash
            remark = '升级' + oldmember.name + '为'+ newmember.name + '会员,扣除金币:' + str(deduct_cash)
            Transactionhistory.objects.create(track=track,memberlevel=oldmember.name,
                                              type='gold',price=deduct_cash,io='O',
                                              overage=cash,pay_by='gold',remark=remark,is_bonus=True)
            bonus.save()
            track.identity = newmember
            track.save()
        else:
            raise ValueError('错误的时机调用')
        
    def transfer_gold(self,accept,goldstr,senduser):
        #判断接收者是否存在，并获取接收者节点信息
        gold = float(goldstr)
        try:
            accept_user = User.objects.get(username=accept)
            accept_track = Doubletrack.objects.get(user=accept_user)
        except ObjectDoesNotExist:
            raise ValueError('accept user is does not exist!')
        else:
            #获取发送用户bonus信息
            send_bonus = Bonus.objects.get(track__user=senduser)
            send_old_cash = send_bonus.cash
            #判断发送用户信息金币是否足够
            if send_old_cash < gold:
                raise ValueError('账户金币不足')
            #获取接收者bonus相关信息
            try:
                accept_bonus = Bonus.objects.get(track=accept_track)
            except ObjectDoesNotExist:
                accept_bonus = init_bonus(accept_track, senduser)
            #开始交易
            ##扣除发送用户金币,并生成交易记录
            send_bonus.cash = F('cash') - gold
            send_bonus.save(update_fields=['cash'])
            remark = "转账至" + accept + ",扣除金币:" + str(gold)
            Transactionhistory.objects.create(track=send_bonus.track,memberlevel=send_bonus.track.identity.name,
                                              type='gold',price=gold,io='O',
                                              overage=send_old_cash,pay_by='gold',remark=remark,is_bonus=True)
            
            ##增加接收用户金币，并生成交易记录
            accept_old_cash = accept_bonus.cash
            accept_bonus.cash = F('cash') + gold
            accept_bonus.save(update_fields=['cash'])
            remark = "接收"+senduser.username + "金币转账,增加金币:" + str(gold)
            Transactionhistory.objects.create(track=accept_track,memberlevel=accept_track.identity.name,
                                              type='gold',price=gold,io='I',
                                              overage=accept_old_cash,pay_by='gold',remark=remark,is_bonus=True)
    
    def withdraw(self,user,bank,bank_account,goldstr):
        gold = float(goldstr)
        track = Doubletrack.objects.get(user=user)
        bonus = Bonus.objects.get(track=track)
        if bonus.cash < gold:
            raise ValueError('账户金币不足')
        else:
            old_bonus = bonus.cash
            bonus.cash = F('cash') - gold
            bonus.save(update_fields=['cash'])
            remark = '用户提现至' + bank + ':' + bank_account
            th = Transactionhistory.objects.create(track=track,memberlevel=track.identity.name,
                                              type='gold',price=gold,io="O",
                                              overage=old_bonus,pay_by='gold',remark=remark,is_bonus=True)
            
            #计算提现税额和提现手续
            from directsales.settings import TAX_RATE,WITHDRAWAL_FEE
            tax = gold * TAX_RATE
            fee = gold * WITHDRAWAL_FEE
            real_price = gold - (tax + fee)
            wh = Withdrawhistory.objects.create(user=user,transaction_related=th,bank=bank,bank_account=bank_account,tax=tax,
                                           fee=fee,price=gold,real_price=real_price,into_account=False)
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
    memberlevel = models.CharField(max_length=30)
    type = models.CharField(max_length=20,choices=TRANSACTION_TYPE)
    price= models.DecimalField(max_digits=18,decimal_places=8)
    io = models.CharField(max_length=1,choices=IO)
    overage = models.DecimalField(max_digits=18,decimal_places=8,blank=True,null=True)
    pay_by=models.CharField(max_length=30,choices=PAY_BY)
    event = models.CharField(max_length=180,blank=True,null=True)
    event_type = models.CharField(max_length=30,blank=True,null=True)
    remark=models.TextField(blank=True,null=True)
    notification = models.NullBooleanField(default=False,blank=True,null=True)
    is_active = models.NullBooleanField(default=True,blank=True,null=True)
    is_bonus = models.NullBooleanField(default=False,blank=True,null=True)
    source_track = models.IntegerField(blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    objects = TransactionhistoryManager()
    def __str__(self):
        return self.track.name
    
class Awards(models.Model):
    name = models.CharField(max_length=30)
    keyword=models.CharField(max_length=20)
    memberlevel = models.ForeignKey(Memberlevel)
    percentage = models.DecimalField(max_digits=4,decimal_places=3)
    seniority_num = models.IntegerField(blank=True,null=True)
    layer_num = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.keyword
    
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
    bank = models.CharField(max_length=60)
    bank_account = models.CharField(max_length=30)
    tax = models.DecimalField(max_digits=18,decimal_places=8)
    fee = models.DecimalField(max_digits=18,decimal_places=8)
    price= models.DecimalField(max_digits=18,decimal_places=8)
    real_price = models.DecimalField(max_digits=18,decimal_places=8)
    into_account = models.NullBooleanField(default=False,blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    