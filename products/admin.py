from django.contrib import admin
from .models import Product, Category, Collection, Extra_Img

# Register your models here.


class ImageInline(admin.StackedInline):

    list_display = [
        'img',
        'id',

    ]

    model = Extra_Img
    readonly_fields = ('id',)
    extra = 0


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'collection',
        'image',
    )

    inlines = (ImageInline, )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
