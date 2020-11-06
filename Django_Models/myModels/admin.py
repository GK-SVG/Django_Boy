from django.contrib import admin
from .models import Student,ExamCenter,AdmitCard,Post,Song
# Register your models here.

admin.site.register(Student)
admin.site.register(ExamCenter)
admin.site.register(AdmitCard)
admin.site.register(Post)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name','song_dur','all_singer']