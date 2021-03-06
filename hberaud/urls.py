from django.conf import settings 
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from home import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^skills/$', views.skills_overview, name='skills'),
    url(r'^skills/(?P<category_slug>[\w-]+)/$', views.skills_overview, name='skills'),
    url(r'^skills/(?P<category_slug>[\w-]+)/(?P<technology_slug>[\w-]+)/$', views.skills_detail, name='skills_detail'),
    url(r'^jobs/$', views.jobs_overview, name='jobs'),
    url(r'^job/(?P<project>[\w-]+)/(?P<client>[\w-]+)/(?P<employer>[\w-]+)/(?P<job>[\w-]+)/(?P<id>[1-9]+)/$',
        views.jobs_detail, name='jobs_detail'),
    url(r'^projects/$', views.projects_overview, name='projects'),
    url(r'^project/(?P<name>[\w-]+)/(?P<id>[\w-]+)/$', views.projects_detail, name='projects_detail'),
    url(r'^curriculum-vitae/$', views.curriculum_vitae, name='curriculum_vitae'),
    url(r'^contact/$', views.contact, name='contact'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()