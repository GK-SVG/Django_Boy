from django.urls import path
from . import views

urlpatterns = [
    path('set/',views.set_session,name='set_session'),
    path('get/',views.get_session,name='get_session'),
    path('del/',views.del_session,name='del_session')
]
