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
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
