'''
Created on 2017-1-30

@author: yimeng
'''
from django.db.models import Manager

from directsales.models import Doubletrack
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
    
