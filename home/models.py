from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    alt_description = models.CharField(max_length=150, default="")
    priority_display = models.IntegerField(default=0)
    active_at_loading = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=80)
    version = models.CharField(max_length=60)
    level = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    usage = models.CharField(max_length=500)
    priority_display = models.IntegerField(default=0)
    tools = models.TextField(max_length=500, default="")
    api = models.TextField(max_length=500, default="")
    icon = models.ImageField(default="", upload_to="technology", blank=True)

    def __str__(self):
        return self.name

    def skills_level(self):
        return self.level * 100 / 5