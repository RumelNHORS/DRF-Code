from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

routers=DefaultRouter()
routers.register('api',views.StudentModelViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routers.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verifytoken'),
]
