from django.contrib import admin

# Register your models here.
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

    # product admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    #list editable means display list in above edit datas
    list_editable = ['price','stock']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
