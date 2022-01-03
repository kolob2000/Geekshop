from django.contrib import admin

from .models import Product, Category, ImageGallery, Contact


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class InlineImage(admin.TabularInline):
    model = ImageGallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_stock')
    list_display_links = ('title', 'category',)
    list_editable = ('is_stock',)
    list_filter = ('category', 'is_stock')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [InlineImage, ]


admin.site.register(Product, ProductAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'phone',)
    list_filter = ('city',)


admin.site.register(Contact, ContactAdmin)
