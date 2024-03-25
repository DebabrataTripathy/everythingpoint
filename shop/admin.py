from django.contrib import admin
from.models import Products,Order

class ProductAdmin(admin.ModelAdmin):

    def ChangeCategory(self,request,queryset):
        queryset.update(category="Default")
    ChangeCategory.short_description="Change category to Default"
    list_display=('name','price','category')
    search_fields=['name']
    actions=['ChangeCategory']
    fields=['name','description','image']
    list_editable=['price','category']
# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
admin.site.site_header="EveryThingPoint"
admin.site.site_title="EveryThingPoint"
admin.site.index_title="EveryThingPoint Control center"

