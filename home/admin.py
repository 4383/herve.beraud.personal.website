from django.contrib import admin
from home.models import Technology
from home.models import Category
from home.models import Framework
from home.models import Version
from home.models import Job
from home.models import Project
from home.models import Company
from home.models import Employer
from home.models import Tasks


class TasksStackedInline(admin.StackedInline):
    model = Tasks


class JobAdmin(admin.ModelAdmin):
    list_display = ("name", "employer", "client", "start_date", "end_date")
    inlines = [TasksStackedInline]


admin.site.register([Category, Technology, Version, Framework,
                     Company, Project, Employer])
admin.site.register(Job, JobAdmin)