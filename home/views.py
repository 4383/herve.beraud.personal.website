from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from home.models import Category
from home.models import Technology
from home.models import Framework
from home.models import Job
from home.models import Project
from home.models import Employer
from home.models import Company
from home.models import Tasks


# Create your views here.
def index(request):
    return render(request, "home/index.html")


# Create your views here.
def skills_overview(request, category='Programming', context={}):
    main_category = get_object_or_404(Category, name=category)
    technologies = Technology.objects.all().filter(category=main_category, active=True).order_by('priority_display')
    context = {'technologies': technologies,
               "main_category": main_category,
               "js_chart_data_label": [technology.name for technology in technologies],
               "js_chart_data_level": [technology.level for technology in technologies], }
    return render(request, "home/skills/overview.html", context)


def skills_detail(request, category, technology, context={}):
    main_technology = get_object_or_404(Technology, name=technology)
    main_category = get_object_or_404(Category, name=category)
    frameworks = Framework.objects.all().filter(active=True, technology=main_technology)
    context = {"main_technology": main_technology,
               "main_category": main_category,
               "max_level": 5,
               "frameworks": frameworks, }
    return render(request, "home/skills/detail.html", context)


def jobs_overview(request):
    jobs = Job.objects.all().order_by('-start_date')
    employers = Employer.objects.all()
    job_distinct = Job.objects.values('client').distinct()
    ids = []
    for dict in job_distinct:
        for key, value in dict.items():
            ids.append(value)
    clients = Company.objects.filter(pk__in=ids)
    context = {"jobs": jobs, "employers": employers, "clients": clients}
    return render(request, "home/jobs/overview.html", context)


def jobs_detail(request, project, client, employer, job, id):
    job = get_object_or_404(Job, id=id)
    tasks = Tasks.objects.all().filter(job__id=id)
    context = {"job": job, "tasks": tasks}
    return render(request, "home/jobs/detail.html", context)


def projects_overview(request):
    projects = Project.objects.all().filter(personal_project=True)
    context = {"projects": projects}
    return render(request, "home/projects/overview.html", context)