from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api import views


router = routers.DefaultRouter()
router.register(r'files', views.FileViewSet)



app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]