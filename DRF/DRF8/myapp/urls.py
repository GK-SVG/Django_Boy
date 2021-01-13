from django.urls import path,include
from rest_framework.routers import DefaultRouter
from myapp.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
# from .tokens import CustumTokenGenerater

router = DefaultRouter()

# router.register('countryAPI',CountryViewset,basename='CountryAPI')
router.register('countryAPI',CountryModelViewset,basename='CountryAPI')
router.register('countryReadOnlyAPI',CountryReadOnlyModelViewset,basename='countryReadOnlyAPI')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refreshtoken/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view())
]
