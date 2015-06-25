from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=500)
    alt_description = models.CharField(max_length=150, default=_("Show more details about this category"))
    priority_display = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Version(models.Model):
    name = models.CharField(max_length=60, unique=True)
    technical_name = models.CharField(max_length=60)
    official_website = models.URLField(blank=True)
    contextual_description = models.CharField(max_length=50, default=_("Show more details about this version"))
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name + " " + self.technical_name


class Technology(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=500)
    contextual_description = models.CharField(max_length=50, default=_("Show more details about this technology"))
    version = models.ManyToManyField(Version, blank=True)
    official_website = models.URLField(blank=True, default="")
    level = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    usage = models.CharField(max_length=500)
    priority_display = models.IntegerField(default=0)
    tools = models.TextField(max_length=500, default="")
    icon = models.ImageField(default="", upload_to="technology", blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def convert_level_in_percent(self):
        return self.level * 100 / 5


class Framework(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=500)
    version = models.ManyToManyField(Version, blank=True)
    technology = models.ForeignKey(Technology)
    contextual_description = models.CharField(max_length=50, default=_("Visit the official website"))
    official_website = models.URLField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name