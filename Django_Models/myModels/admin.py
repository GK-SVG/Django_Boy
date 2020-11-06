from django.contrib import admin
from .models import Student,ExamCenter,AdmitCard,Post
# Register your models here.

admin.site.register(Student)
admin.site.register(ExamCenter)
admin.site.register(AdmitCard)
admin.site.register(Post)