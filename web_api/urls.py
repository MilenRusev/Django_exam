from django.conf.urls import url, include
from rest_framework import routers
from accounts.views import AccountViewSet
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', AccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
