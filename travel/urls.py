from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, viewsets
from app.models import App
from app.serializers import AppSerializer
from category.models import Category
from category.serializers import CategorySerializer
from country.models import Country
from country.serializers import CountrySerializer
from .permissions import IsAdminOrReadOnly


class AppViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = App.objects.all()
    serializer_class = AppSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

router = routers.DefaultRouter()
router.register(r'app', AppViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'country', CountryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
