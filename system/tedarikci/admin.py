from django.contrib import admin

from .models import Supplier

# Register your models here.


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ["company_name","contact_name","register_time"]

    list_display_links = ["company_name","contact_name","register_time"]

    search_fields = ["company_name"]

    list_filter = ["register_time"]
    class Meta:
        model = Supplier