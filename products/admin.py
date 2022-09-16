from django.contrib import admin

from .models import Product,Review
readonly_fields = ("create_date")




class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock",)
    list_display_links = ("create_date", )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)     


admin.site.register(Product,ProductAdmin )    
admin.site.register(Review,ReviewAdmin)    



admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"

