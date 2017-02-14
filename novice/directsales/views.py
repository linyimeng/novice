from io import BytesIO

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db import transaction
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as djangologout,authenticate,login as djangologin
from django.utils.timezone import now,timedelta

from directsales.models import Doubletrack,Transactionhistory, Memberlevel,Withdrawhistory,Order,Goods,Orderdetail
from directsales.forms import DoubletrackForm,AddressForm
from directsales.ajaxchk import isenough
from directsales.verifycode import VerifyCode
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def login(request):
    '''登录'''
    if request.method=="GET":
        return render(request,"directsales/login.html")
    elif request.method=="POST":
        user = authenticate(username = request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                djangologin(request, user)
                return redirect('/directsale/home')
            else:
                return redirect('/directsale/login')
        else:
            return redirect('/directsale/login')
        
def verifycode(request):
    '''验证码'''
    vecode=VerifyCode()
    code_img,capacha_code= vecode.createCodeImage();
    request.session['code'] = capacha_code
    msstream=BytesIO()
    code_img.save(msstream,"jpeg")
    code_img.close()
    return HttpResponse(msstream.getvalue(),content_type='image/jpg')


@login_required(login_url='/directsale/login/')
def logout(request):
    '''登出'''
    djangologout(request)
    return redirect('/directsale/login')

@login_required(login_url='/directsale/login/')
def changepassword(request):
    if request.method == "GET":
        return render(request,"directsales/changepassword.html")
    elif request.method=="POST":
        user = authenticate(username = request.user.username, password=request.POST.get('oldpwd'))
        if user is not None:
            user.set_password(request.POST.get('newpwd'))
            user.save()
            return redirect("/directsale/success/changepassword")
        else:
            return render(request,"directsales/changepassword.html")
        
@login_required(login_url='/directsale/login/')
def changepaypassword(request):
    if request.method=="GET":
        return render(request,"directsales/changepaypassword.html")
    elif request.method == "POST":
        track = Doubletrack.objects.get(user=request.user)
        oldpaypwd = request.POST.get('oldpaypwd')
        newpaypwd = request.POST.get('newpaypwd')
        if track.pay_password == oldpaypwd:
            track.pay_password = newpaypwd
            track.save()
            return redirect("/directsale/success/changepassword")
        else:
            return render(request,"directsales/changepaypassword.html")
            

@login_required(login_url='/directsale/login/')
def view_home(request):
    '''主页'''
    start = now().date()
    end = start + timedelta(days=1)
    gold = Transactionhistory.objects.filter(type="gold",io='I',track__user=request.user,joined__range=(start,end)).aggregate(gold=Sum('price'))
    integral = Transactionhistory.objects.filter(type="integral",io='I',track__user=request.user,joined__range=(start,end)).aggregate(integral=Sum('price'))
    shoppingcoupons = Transactionhistory.objects.filter(type="shoppingcoupons",io='I',track__user=request.user,joined__range=(start,end)).aggregate(shoppingcoupons=Sum('price'))
    return render(request,"directsales/index.html",{"gold":gold,"integral":integral,"shoppingcoupons":shoppingcoupons})

@login_required(login_url='/directsale/login/')
@transaction.atomic
def registered(request,parentusername=None,isright=None):
    '''注册'''
    if request.method=="GET":
        return render(request,"directsales/registered.html",{'parent':parentusername,'isright':isright})
    else:
        formdata = request.POST.copy()
        #验证金币是否足够
        identity_id = formdata.get('identity')
        if not isenough(identity_id,request.user):
            return HttpResponse('金币不足，无法完成注册;请勿关闭客户端验证')
        #创建用户
        try:
            user = User.objects.create_user(username=formdata.get('username'),email=formdata.get('email'),
                                            password=formdata.get('password'))
        except IntegrityError:
            return HttpResponse('注册信息错误或用户已存在;请勿关闭客户端验证')
        else:
            user.is_active = True
            user.save()
            formdata['user'] = user.pk
        #验证父节点
        try:
            parent_user = User.objects.get(username=formdata.get('parent'))
        except ObjectDoesNotExist:
            return HttpResponse('节点用户不存在;请勿关闭客户端验证')
        else:
            formdata['parent'] = Doubletrack.objects.get(user=parent_user).pk
        #验证直推节点
        try:
            directpushuser = User.objects.get(username=formdata.get('directpushuser'))
        except ObjectDoesNotExist:
            return HttpResponse('直推者不存在;请勿关闭客户端验证')
        else:
            formdata['directpushuser'] = Doubletrack.objects.get(user=directpushuser).pk
            formdata['creator'] = request.user.pk
            formdata['is_active'] = True
        #保存注册信息
        form = DoubletrackForm(formdata)
        if form.is_valid():
            form.save()
            #保存成功后扣除金币
            Transactionhistory.objects.registered_deduct_gold(identity_id, request.user,user)
            return render(request,"directsales/success/reg_to_other.html",{"reg_user":user})
        else:
            return HttpResponse(form.errors)

@login_required(login_url='/directsale/login/')
@transaction.atomic
def upgrade_member(request):
    '''升级会员'''
    if request.method == "GET":
        #获取当前用户点位信息
        track = Doubletrack.objects.get(user=request.user)
        memberlevel = Memberlevel.objects.all()
        return render(request,"directsales/upgrade_member.html",{"track":track,"memberlevel":memberlevel})
    elif request.method=="POST":
        upgrade_identity_id = request.POST.get('identity')
        if not isenough(upgrade_identity_id,request.user):
            return HttpResponse('金币不足，无法完成注册;请勿关闭客户端验证')
        else:
            #扣除金币，升级会员
            Transactionhistory.objects.upgrade_deduct_gold(upgrade_identity_id,request.user)
            return redirect("/directsale/success/upgrade_member")
        
@login_required(login_url='/directsale/login/')
@transaction.atomic
def transfer(request):
    '''资金转账'''
    if request.method == "GET":
        return render(request,"directsales/transfer.html")
    elif request.method == "POST":
        transaction_type = request.POST.get('transaction_type')
        accept = request.POST.get('accept')
        num = request.POST.get('num')
        Transactionhistory.objects.transfer(accept, num, request.user, transaction_type)
        return redirect('/directsale/success/transfer_gold')
    
@login_required(login_url='/directsale/login/')
def view_member_list(request):
    '''会员列表'''
    try:
        track = Doubletrack.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return HttpResponse('not')
    member_list = Doubletrack.objects.get_track_child_list(track)
    return render(request, "directsales/member_list.html",{"member_list":member_list})

@login_required(login_url='/directsale/login/')
def view_member_tree(request,username=None):
    username = request.GET.get('username',username)
    if username is None:
        user = request.user
    else:
        try:
            user = User.objects.get(username=username)
        except:
            return(request,"directsales/500.html")
    try:
        track = Doubletrack.objects.get(user=user)
        track0 = Doubletrack.objects.get_member_info(track)[0]
        
    except ObjectDoesNotExist:
        return render(request,"directsales/500.html")
    try:
        track1 = Doubletrack.objects.get_member_info('',parent=track0,isright=False)[0]
    except ObjectDoesNotExist:
        track1 = None
        
    try:
        track2 = Doubletrack.objects.get_member_info('',parent=track0,isright=True)[0]
    except ObjectDoesNotExist:
        track2 = None
        
    try:
        track3 = Doubletrack.objects.get_member_info('',parent=track1,isright=False)[0]
    except ObjectDoesNotExist:
        track3 = None
        
    try:
        track4 = Doubletrack.objects.get_member_info('',parent=track1,isright=True)[0]
    except ObjectDoesNotExist:
        track4 = None
        
    try:
        track5 = Doubletrack.objects.get_member_info('',parent=track2,isright=False)[0]
    except ObjectDoesNotExist:
        track5 = None
        
    try:
        track6 = Doubletrack.objects.get_member_info('',parent=track2,isright=True)[0]
    except ObjectDoesNotExist:
        track6 = None
    return render(request,"directsales/member_tree.html",{"track0":track0,"track1":track1,"track2":track2,"track3":track3,"track4":track4,
                                                          "track5":track5,"track6":track6})


@login_required(login_url='/directsale/login/')
def view_bonus_detail(request):
    '''资金明细'''
    Transactionhistory.objects.filter(track__user=request.user).update(notification=True)
    transaction_history = Transactionhistory.objects.filter(track__user=request.user)
    gold_history = transaction_history.filter(type="gold").order_by('-joined')
    integral_history = transaction_history.filter(type="integral").order_by('pk')
    shoppingcoupons_history = transaction_history.filter(type="shoppingcoupons").order_by('pk') 
    return render(request,"directsales/transaction_history.html",{'transaction_history':transaction_history,
                                                                  'gold_history':gold_history,
                                                                  'integral_history':integral_history,
                                                                  'shoppingcoupons_history':shoppingcoupons_history,
                                                                })

@login_required(login_url='/directsale/login/')
def view_withdrawal_history(request):
    withdrawal_history = Withdrawhistory.objects.filter(user=request.user)
    return render(request,"directsales/withdrawal_history.html",{'withdrawal_history':withdrawal_history,})

@login_required(login_url='/directsale/login/')
@transaction.atomic
def gold_withdrawal(request):
    '''金币提现'''
    if request.method == "GET":
        from directsales.settings import TAX_RATE,WITHDRAWAL_FEE
        track = Doubletrack.objects.values('bank','bank_account').get(user=request.user)
        return render(request,"directsales/gold_withdrawals.html",{'track':track,'tax_rate':TAX_RATE*100,'fee':WITHDRAWAL_FEE*100})
    elif request.method == "POST":
        #防止重复提交
        bank = request.POST.get('bank')
        bank_account = request.POST.get('bank_account')
        goldstr = request.POST.get('gold')
        withdrawal = Transactionhistory.objects.withdraw(request.user, bank, bank_account, goldstr)
        return redirect('/directsale/goldwithdrawal/success/%s'%(withdrawal.pk))

def gold_withdrawal_success(request,wh_pk):
    #防提交重复
    withdrawal = get_object_or_404(Withdrawhistory,pk=wh_pk)
    try:
        subject = "金币提现" + "_" + request.user.username + "_请及时处理"
        to_email = "yimeng88@loongkylin.com"#"billing@globalbraincapital.com"
        message = "提现用户："+ request.user.username + "银行:"+withdrawal.bank + ",帐号:"+ withdrawal.bank_account+ "，提现金额:￥"+str("%.2f"%withdrawal.price)+"，税额:￥"+\
                  str("%.2f"%withdrawal.tax)+"提现手续费:￥"+ str("%.2f"%withdrawal.fee) + ",预计到帐金额："+ str("%.2f"%(withdrawal.real_price)) +"，提现时间：" + withdrawal.joined.strftime("%Y-%m-%d %H:%M:%S")
        from mailroom.models import Emailhistory
        Emailhistory.objects.send_mail_save(user=request.user,subject=subject,message=message,from_email='yimeng88@loongkylin.com',
                                           to_email=to_email)
    except:
        pass
    return render(request, "directsales/success/withdrawal.html",{'withdrawal':withdrawal})


@login_required(login_url='/directsale/login/')
@transaction.atomic
def doubletrackInfo(request):
    if request.method=="GET":
        track = Doubletrack.objects.get(user=request.user)
        return render(request,"directsales/track_info.html",{"track":track})
    elif request.method=="POST":
        track = Doubletrack.objects.get(user=request.user)
        track.name = request.POST.get('name')
        track.address = request.POST.get('address')
        track.bank = request.POST.get('bank')
        track.bank_account = request.POST.get('bank_account')
        track.save()
        return redirect("/directsale/success/trackinfo")

@login_required(login_url='/directsale/login/')
def send_email(request):
    if request.method=="GET":
        return render(request,"directsales/send_mail.html")
    else:
        subject1 = request.POST.get('subject')
        message = request.POST.get('message')
        track = Doubletrack.objects.get(user=request.user)
        if subject1=="billing":
            to_email = 'billing@globalbraincapital.com'
            message = message + "\n\n\n用户名：" + request.user.username + "， 姓名："+ track.name + ", 手机:" + track.phone
        elif subject1=="feedback":
            to_email = "feedback@globalbraincapital.com"
        else:
            to_email = "feedback@globalbraincapital.com"
        subject = subject1 + "_" + request.user.username + "_申请，请及时处理"
        
        from mailroom.models import Emailhistory
        Emailhistory.objects.send_mail_save(user=request.user,subject=subject,message=message,from_email='yimeng88@loongkylin.com',
                                           to_email=to_email)
        return redirect("/directsale/success/send_mail")

@login_required(login_url='/directsale/login/')
def bulletin_board(request):
    from directsales.models import Bulletin_board
    bulletins = Bulletin_board.objects.all().order_by('-joined')[:10]
    return render(request,"directsales/bulletin_board.html",{"bulletins":bulletins})

def page_not_found(request):
    return render(request,"directsales/404.html")

def page_error(request):
    return render(request,"directsales/500.html")

def success(request,template_path):
    template_path = 'directsales/success/'+template_path + ".html"
    return render(request,template_path)

@login_required(login_url='/directsale/login/')
def view_goods(request):
    from mall.models import Shippingaddress
    goodss = Goods.objects.all()[:8]
    addresses = Shippingaddress.objects.filter(user=request.user).order_by('-joined')[:8]
    return render(request,"directsales/goods.html",{"addresses":addresses,"goodss":goodss})


@login_required(login_url='/directsale/login/')
def add_address(request):
    formdata = request.POST.copy()
    formdata["user"] = request.user.pk
    form = AddressForm(formdata)
    if form.is_valid():
        form.save()
        return redirect("/directsale/goods")
    else:
        return HttpResponse(form.errors)
    
@login_required(login_url='/directsale/login/')
@csrf_exempt
@transaction.atomic
def createorder(request):
    from json import dumps
    pay_by = request.POST.get('pay_by')
    addresspk = request.POST.get('address')
    jsonstr = request.POST.get('goodsdetail')
    ordercode = Order.objects.create_order(pay_by, addresspk, jsonstr,request.user)
    return HttpResponse(dumps({'result':True,"ordercode":ordercode}),content_type='application/json')
    
@login_required(login_url='/directsale/login/')
def createorder_success(request,ordercode):
    order = Order.objects.get(ordercode=ordercode)
    return render(request,"directsales/success/order.html",{"order":order})

def orderhistory(request):
    orders = Order.objects.filter(user=request.user).order_by('-joined')
    return render(request,"directsales/order_history.html",{"orders":orders})
    
def orderdetail(request,ordercode):
    order = Order.objects.get(ordercode=ordercode)
    orderdetail = Orderdetail.objects.filter(ordercode = order)
    return render(request,"directsales/orderdetail.html",{"order":order,"details":orderdetail})
    
def shipgoods(request):
    detail = Orderdetail.objects.filter(supplier__user=request.user)
    ship = detail.filter(status='ship').order_by('-updated')
    pay = detail.filter(status='pay').order_by('-joined')
    return render(request,"directsales/shipgoods.html",{'ship':ship,'pay':pay})
    
    
    