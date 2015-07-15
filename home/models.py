from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
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
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + " " + self.technical_name


class Technology(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
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
    description = models.TextField()
    version = models.ManyToManyField(Version, blank=True)
    technology = models.ForeignKey(Technology)
    contextual_description = models.CharField(max_length=50, default=_("Visit the official website"))
    official_website = models.URLField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    contextual_description = models.CharField(max_length=100)
    technology = models.ManyToManyField(Technology)
    framework = models.ManyToManyField(Framework, blank=True)
    tasks = models.CharField(max_length=300)
    url = models.URLField(default="")
    personal_project = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=150, unique=True, default="")
    description = models.TextField(max_length=300, default="")
    contextual_description = models.CharField(max_length=100, default="")
    logo = models.ImageField(default="", upload_to="employer", blank=True)
    location = models.CharField(max_length=100, default="")
    official_website = models.URLField(default="")

    def __str__(self):
        return self.name


class Employer(Company):
    projects = models.ManyToManyField(Project, through="Job")
    current_employer = models.BooleanField(default=False)


class Job(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=500)
    contextual_description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project)
    employer = models.ForeignKey(Employer, related_name="employer", default=None)
    client = models.ForeignKey(Company, related_name="client", default=None)

    def __str__(self):
        return self.name

    def generate_url(self):
        return self.name.replace(" ", "+").lower()
