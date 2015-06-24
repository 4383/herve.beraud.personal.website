from django.contrib import admin
from home.models import Technology
from home.models import Category
from home.models import Framework
from home.models import Version


class TechhnologyAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class VersionAdmin(admin.ModelAdmin):
    pass


class FrameworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechhnologyAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Framework, FrameworkAdmin)
