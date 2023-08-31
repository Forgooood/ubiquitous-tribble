import django.contrib
from mptt.admin import MPTTModelAdmin

from catalog.models import Category, Product, Review


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30


django.contrib.admin.site.register(Category, CustomMPTTModelAdmin)


@django.contrib.admin.register(Product)
class ProductAdmin(django.contrib.admin.ModelAdmin):
    list_display = ('title', 'category',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('category',)


@django.contrib.admin.register(Review)
class ReviewAdmin(django.contrib.admin.ModelAdmin):
    list_display = ('name', 'product', 'rating',)
