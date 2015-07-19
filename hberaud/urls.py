from django.conf import settings 
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hberaud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^skills/$', views.skills_overview, name='skills'),
    url(r'^skills/(?P<category>[\w-]+)/$', views.skills_overview, name='skills'),
    url(r'^skills/(?P<category>[\w-]+)/(?P<technology>.*)/$', views.skills_detail, name='skills_detail'),
    url(r'^jobs/$', views.jobs_overview, name='jobs'),
    url(r'^job/(?P<project>[\w-]+)/(?P<client>[\w-]+)/(?P<employer>[\w-]+)/(?P<job>[\w-]+)/(?P<id>[1-9]+)/$', views.jobs_detail, name='jobs_detail'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)