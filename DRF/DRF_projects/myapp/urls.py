from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',include('djoser.urls'),name="Djoser"),
    path("",include("djoser.urls.authtoken")),
    path('verifyUser/',views.index,name="Index")
]
