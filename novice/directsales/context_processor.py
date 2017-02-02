'''
Created on 2017-1-27

@author: yimeng
'''
from directsales.models import Bonus,Doubletrack,Transactionhistory,init_bonus
from django.core.exceptions import ObjectDoesNotExist

def get_bonus(request):
    '''如bonus表中无记录，但Doubletrack表中有记录，则插入数据'''
    if request.user.is_authenticated():
        try:
            track = Doubletrack.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return {}
        else:
            try:
                bonus = Bonus.objects.get(track=track)
            except ObjectDoesNotExist:
                bonus = init_bonus(track, request.user)
        notification = Transactionhistory.objects.get_notification(request.user)
        return {'bonus':bonus,'notification':notification}
    else:
        return {}