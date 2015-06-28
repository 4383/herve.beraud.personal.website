__author__ = 'herve'
from django import template
from home.models import Category
from home.models import Technology

register = template.Library()


@register.inclusion_tag('home/extra/categories_menu.html', takes_context=True)
def show_categories_menu(context):
    categories = Category.objects.all().filter(active=True).order_by('priority_display')
    return {"categories": categories, "active": context["main_category"]}

@register.inclusion_tag('home/extra/technologies_menu.html', takes_context=True)
def show_technologies_menu(context):
    technologies = Technology.objects.all().filter(category=context['main_category'], active=True).order_by('priority_display')
    return {"technologies": technologies}
