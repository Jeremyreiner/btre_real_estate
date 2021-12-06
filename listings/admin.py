from django.contrib import admin
from .models import Listing
# Register your models here.

@admin.register(Listing) #decorator
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'stats', 'zipcode', 'price')
    list_per_page = 20


# admin.site.register(Listing) #if using decorater no need for this line