from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    ordering = ('name', )


admin.site.register(Order, OrderAdmin)
