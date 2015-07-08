from django.contrib import admin
from home.models import Technology
from home.models import Category
from home.models import Framework
from home.models import Version
from home.models import Job
from home.models import Project
from home.models import Company
from home.models import Employer


admin.site.register([Category, Technology, Version, Framework,
                     Job, Company, Project, Employer])