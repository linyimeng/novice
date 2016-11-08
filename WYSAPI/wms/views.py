from rest_framework.generics import ListAPIView
from order.models import Detail
from wms.serializers import GoodsListSerializer
# Create your views here.

class GoodsListAPIView(ListAPIView):
    queryset = Detail.objects.all().distinct('goods')
    serializer_class = GoodsListSerializer
