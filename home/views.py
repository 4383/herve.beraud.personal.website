from django.http import Http404
from django.shortcuts import render
from home.models import Category
from home.models import Technology
from home.models import Framework


# Create your views here.
def index(request):
    return render(request, "home/index.html")


# Create your views here.
def skills_overview(request, category='Programming', context={}):
    main_category = Category.objects.get(name=category)
    # Les technologies associées aux catégories afin de générer le contenu
    technologies = Technology.objects.all().filter(category=main_category, active=True).order_by('priority_display')
    js_chart_data_label = []
    js_chart_data_level = []
    for technology in technologies:
        js_chart_data_label.append(technology.name)
        js_chart_data_level.append(technology.level)
    context = {'technologies': technologies,
               "main_category": main_category,
               "chart_data_label": js_chart_data_label,
               "chart_data_level": js_chart_data_level, }
    return render(request, "home/skills/overview.html", context)


def skills_detail(request, category, technology, context={}):
    try:
        main_technology = Technology.objects.get(name=technology)
        main_category = Category.objects.get(name=category)
        frameworks = Framework.objects.all().filter(active=True, technology=main_technology)
        context = {"main_technology": main_technology,
                   "main_category": main_category,
                   "max_level": 5,
                   "frameworks": frameworks, }
    except Technology.DoesNotExist:
        raise Http404("Technology does not exist. Page not found")
    except Category.DoesNotExist:
        raise Http404("Category does not exist. Page not found")
    return render(request, "home/skills/detail.html", context)


def jobs_overview(request):
    return render(request, "home/jobs/overview.html")


def jobs_detail(request, name):
    return render(request, "home/jobs/detail.html")
