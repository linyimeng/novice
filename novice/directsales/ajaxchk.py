'''
Created on 2017-1-14

@author: yimeng
'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from json import dumps
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from directsales.models import Doubletrack,Bonus,Memberlevel
@csrf_exempt
def chkUser(request):
    username = request.POST.get('username')
    try:
        user = User.objects.get(username=username)
        if request.user.is_authenticated():
            track = Doubletrack.objects.get(user=user)
            trackname = track.name
        else:
            trackname = None
    except ObjectDoesNotExist:
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False,'username':user.username,'trackname':trackname}),content_type='application/json')

@csrf_exempt   
def chkpwd(request):
    user = authenticate(username = request.user.username, password=request.POST.get('password'))
    if user is not None:
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False}),content_type='application/json')

@csrf_exempt   
def chkpaypwd(request):
    track = Doubletrack.objects.get(user=request.user)
    print(track.pay_password)
    print(request.POST.get('oldpaypwd'))
    if track.pay_password == request.POST.get('oldpaypwd'):
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False}),content_type='application/json')

@csrf_exempt   
def chkdoubletrack(request):
    username = request.POST.get('username')
    if Doubletrack.objects.checking_istrack(username):
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False}),content_type='application/json')
    
@csrf_exempt   
def chkparenttrack(request):
    username = request.POST.get('username')
    if Doubletrack.objects.checking_istrack(username):
        user = User.objects.get(username=username)
        if Doubletrack.objects.checking_doubletrack(user):
            return HttpResponse(dumps({'result':True}),content_type='application/json')
        else:
            return HttpResponse(dumps({'result':False}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False}),content_type='application/json')
    
@csrf_exempt
def chkisright(request):
    isright = request.POST.get('isright')
    username = request.POST.get('username')
    if isright=="true":
        isright = True
    else:
        isright = False
    user = User.objects.get(username=username)
    track = Doubletrack.objects.get(user=user)
    child = Doubletrack.objects.filter(parent=track)
    child_count = child.count()
    if child_count == 0:
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    elif child_count == 1:
        if child[0].isright is isright:
            return HttpResponse(dumps({'result':False,'recommend':not isright}),content_type='application/json')
        else:
            return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False,'recommend':not isright}),content_type='application/json')
    
@csrf_exempt
def chkisenough(request):
    identity_id = request.POST.get('identity_id')
    #获取当前用户gold的余额
    track = Doubletrack.objects.get(user = request.user)
    gold = Bonus.objects.get(track=track).gold
    #获取当前所需的现金
    need_gold = Memberlevel.objects.get(pk=identity_id).price
    if gold >= need_gold:
        print(identity_id)
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False}),content_type='application/json')
    
@csrf_exempt
def chkverifycode(request):
    code = request.POST.get('code')
    verify_code = request.session.get('code')
    if code == verify_code:
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':False}),content_type='application/json')
    
@csrf_exempt
def confirmpay(request):
    paypws = request.POST.get('paypwd')
    try:
        Doubletrack.objects.get(user=request.user,pay_password=paypws)
    except ObjectDoesNotExist:
        return HttpResponse(dumps({'result':False}),content_type='application/json')
    else:
        return HttpResponse(dumps({'result':True}),content_type='application/json')
    
def isenough(identity_id,user):
    track = Doubletrack.objects.get(user = user)
    gold = Bonus.objects.get(track=track).gold
    #获取当前所需的现金
    need_gold = Memberlevel.objects.get(pk=identity_id).price
    if gold >= need_gold:
        return True
    else:
        return False
    

    
    
    
    