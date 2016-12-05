from file.serializers import ImgSerializer
# Create your views here.
from rest_framework.generics import CreateAPIView

class ImageCreateAPIView(CreateAPIView):
    serializer_class = ImgSerializer