from django.contrib import admin
from .models import Country
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['id','name','capital','population']