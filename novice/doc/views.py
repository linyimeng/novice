from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(('GET',))
def api_root(request,format=None):
    return Response({
        '用户':reverse('user-doc',request=request,format=format),
        '部门和员工':reverse('emp-doc',request=request, format=format),
        '供应商和客户(合作伙伴)':reverse('partner-doc',request=request,format=format),
        '商品':reverse('goods-doc',request=request,format=format),
        '订单':reverse('order-doc',request=request,format=format),
    })