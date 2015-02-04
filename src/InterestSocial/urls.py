from django.conf.urls import patterns, include, url
from InterestSocial import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


def v1_w_url(regex, view, kwargs=None, name=None, prefix=''):
    url_prefix = '^'+settings.URL_PREFIX['v1_w']
    regex = url_prefix+regex
    return url(regex, view, kwargs, name, prefix)

def v1_r_url(regex, view, kwargs=None, name=None, prefix=''):
    url_prefix = '^'+settings.URL_PREFIX['v1_r']
    regex = url_prefix+regex
    return url(regex, view, kwargs, name, prefix)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InterestSocial.views.home', name='home'),
    # url(r'^InterestSocial/', include('InterestSocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #===========================================================================
    # write API
    #===========================================================================
    v1_w_url(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
    v1_w_url(r'people/', include('people.w_urls', namespace='people')),
    
    
    #===========================================================================
    # read API
    #===========================================================================
    v1_r_url(r'people/', include('people.r_urls', namespace='people')),
)
