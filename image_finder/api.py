from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import ImageHeader,ImageDetail

router = routers.DefaultRouter()

class ImageHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageHeader
        fields = ('id','description', 'date_added', 'resolved')
class ImageHeaderViewSet(viewsets.ModelViewSet):
    queryset = ImageHeader.objects.all()
    serializer_class = ImageHeaderSerializer
router.register(r'image_header', ImageHeaderViewSet)

class ImageDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageDetail
        fields = ('id','image_header', 'image', 'resolved')
class ImageDetailViewSet(viewsets.ModelViewSet):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer
router.register(r'image_detail', ImageDetailViewSet)
