from django.contrib import admin
from home.models import Technology
from home.models import Category


class TechhnologyAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechhnologyAdmin)
