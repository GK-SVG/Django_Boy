from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from myapp.views import MovieViewset,CrewViewset

router = DefaultRouter()

router.register('movie',MovieViewset,basename='Movies')
router.register('crew',CrewViewset,basename='Crew')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
