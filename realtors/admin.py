from django.contrib import admin
from .models import Realtor
# Register your models here.

@admin.register(Realtor) #class decorater
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


# admin.site.register(Realtor) #needs to be at bottem &no need if theres a class decorater