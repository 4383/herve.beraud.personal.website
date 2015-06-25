from django.shortcuts import render
from home.models import Category
from home.models import Technology
from home.models import Framework


# Create your views here.
def index(request):
    return render(request, "home/index.html")


# Create your views here.
def skills(request, category='Programming', context={}):
    main_category = Category.objects.get(name=category)
    # Les categories pour construire le menu
    categories = Category.objects.all().filter(active=True).order_by('priority_display')
    # Les technologies associées aux catégories afin de générer le contenu
    technologies = Technology.objects.all().filter(category=main_category, active=True).order_by('priority_display')
    chart_data_label = []
    chart_data_level = []
    for technology in technologies:
        chart_data_label.append(technology.name)
        chart_data_level.append(technology.level)
    context = {'categories': categories,
               'technologies': technologies,
               "main_category": main_category,
               "chart_data_label": chart_data_label,
               "chart_data_level": chart_data_level, }
    return render(request, "home/skills.html", context)


def detailed_skills(request, category, technology, context={}):
    main_category = Category.objects.get(name=category)
    # Les categories pour construire le menu
    categories = Category.objects.all().order_by('priority_display')
    # Les technologies associées aux catégories afin de générer le contenu
    main_technology = Technology.objects.get(name=technology)
    technologies = Technology.objects.all().filter(category=main_category).order_by('priority_display')
    frameworks = Framework.objects.all().filter(active=True, technology=main_technology)
    context = {'categories': categories,
               'main_technology': main_technology,
               "technologies": technologies,
               "main_category": main_category,
               "max_level": 5,
               "frameworks": frameworks, }
    return render(request, "home/detailed_skills.html", context)
