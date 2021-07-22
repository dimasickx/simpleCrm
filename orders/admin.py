from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'type', 'status')
    pass

# admin.site.register(Order)
