from django.contrib import admin
from .models import Movie,Crew
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name','rel_date']

@admin.register(Crew)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','movie','actor','acteress']