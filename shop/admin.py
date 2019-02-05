from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    # Any field in the list_editable attribute must be in the list_display attribute,
    # since only the fields displayed can be edited
    list_editable = ['price', 'stock', 'available']
    # we are using prepopulated_fields attribute to specify fields where the value
    # is automatically set using the value of another field
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
