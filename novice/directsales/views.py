from io import BytesIO

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as djangologout,authenticate,login as djangologin
from django.utils.timezone import now,timedelta

from directsales.models import Doubletrack,Transactionhistory, Memberlevel,Bonus,Withdrawhistory
from directsales.forms import DoubletrackForm
from directsales.ajaxchk import isenough
from directsales.verifycode import VerifyCode

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
                print(request.user)
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
            return render(request,"directsales/success/changepassword.html")
        else:
            return render(request,"directsales/changepassword.html")

@login_required(login_url='/directsale/login/')
def view_home(request):
    '''主页'''
    start = now().date()
    end = start + timedelta(days=1)
    try:
        today_bonus = Bonus.objects.get(track__user=request.user,joined__range=(start,end))
    except ObjectDoesNotExist:
        today_bonus = {"cash":0,"integral":0,"shoppingcoupons":0}
    return render(request,"directsales/index.html",{"today_bonus":today_bonus})

@login_required(login_url='/directsale/login/')
@transaction.atomic
def registered(request):
    '''注册'''
    if request.method=="GET":
        return render(request,"directsales/registered.html",{})
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
        #保存注册信息
        form = DoubletrackForm(formdata)
        if form.is_valid():
            form.save()
            #保存成功后扣除金币
            Transactionhistory.objects.registered_deduct_cash(identity_id, request.user,user)
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
            Transactionhistory.objects.upgrade_deduct_cash(upgrade_identity_id,request.user)
            return render(request,"directsales/success/upgrade_member.html")
        
@login_required(login_url='/directsale/login/')
@transaction.atomic
def transfer_gold(request):
    '''现金转账'''
    if request.method == "GET":
        return render(request,"directsales/transfer_gold.html")
    elif request.method == "POST":
        accept = request.POST.get('accept')
        gold = request.POST.get('gold')
        Transactionhistory.objects.transfer_gold(accept,gold,request.user)
        return render(request,'directsales/success/transfer_gold.html')
    
@login_required(login_url='/directsale/login/')
def view_member_list(request):
    '''会员列表'''
    try:
        track = Doubletrack.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return HttpResponse('not')
    member_list = Doubletrack.objects.get_track_child_list(track)
    return render(request, "directsales/member_list.html",{"member_list":member_list})

def view_member_tree(request):
    return render(request,"directsales/gojs_tree.html")


@login_required(login_url='/directsale/login/')
def view_bonus_detail(request):
    '''资金明细'''
    Transactionhistory.objects.filter(track__user=request.user).update(notification=True)
    transaction_history = Transactionhistory.objects.filter(track__user=request.user)
    cash_history = transaction_history.filter(type="gold").order_by('pk')
    integral_history = transaction_history.filter(type="integral").order_by('pk')
    shoppingcoupons_history = transaction_history.filter(type="shoppingcoupons").order_by('pk') 
    return render(request,"directsales/transaction_history.html",{'transaction_history':transaction_history,
                                                                  'cash_history':cash_history,
                                                                  'integral_history':integral_history,
                                                                  'shoppingcoupons_history':shoppingcoupons_history,
                                                                })


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
        bank = request.POST.get('bank')
        bank_account = request.POST.get('bank_account')
        goldstr = request.POST.get('gold')
        withdrawal = Transactionhistory.objects.withdraw(request.user, bank, bank_account, goldstr)
        return render(request, "directsales/success/withdrawal.html",{'withdrawal':withdrawal})
        
@login_required(login_url='/directsale/login/')
@transaction.atomic
def doubletrackInfo(request):
    if request.method=="GET":
        track = Doubletrack.objects.get(user=request.user)
        return render(request,"directsales/track_info.html",{"track":track})
    elif request.method=="POST":
        track = Doubletrack.objects.get(user=request.user)
        track.address = request.POST.get('address')
        track.bank = request.POST.get('bank')
        track.bank_account = request.POST.get('bank_account')
        track.save()
        return render(request,"directsales/success/trackinfo.html")


def page_not_found(request):
    return render(request,"directsales/404.html")

def page_error(request):
    return render(request,"directsales/500.html")


def send_email(request):
    from django.core.mail import send_mail

    send_mail('Subject here', 'Here is the message.', 'yimeng88@loongkylin.com',
        ['yimeng88@loongkylin.com'], fail_silently=False)
    return HttpResponse('ok')

