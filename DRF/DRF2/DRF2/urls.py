
from django.contrib import admin
from django.urls import path
from myapp.views import employee_api,EmployeeAPI
from myapp2.views import StudentAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeData/',employee_api),
    path('ClassemployeeData/',EmployeeAPI.as_view()),
    path('StudentAPI/',StudentAPI.as_view())
]
