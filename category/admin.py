from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)