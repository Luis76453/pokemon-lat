from django.contrib import admin
from .models import Owner


#admin.site.register(Owner)
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("nombre","edad","pais",)
    list_filter = ("edad",)
    search_fields = ("nombre","pais",)
    #fields = ("nombre","dni",)