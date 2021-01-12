from django.urls import path,include
from rest_framework.routers import DefaultRouter
from myapp.views import *
# from .tokens import CustumTokenGenerater

router = DefaultRouter()

# router.register('countryAPI',CountryViewset,basename='CountryAPI')
router.register('countryAPI',CountryModelViewset,basename='CountryAPI')
router.register('countryReadOnlyAPI',CountryReadOnlyModelViewset,basename='countryReadOnlyAPI')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    # path('gettoken/',CustumTokenGenerater.as_view())
]
