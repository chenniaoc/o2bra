from django.conf.urls import patterns, include, url
from o2bra_cms.collections import urls as collection_urls

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'o2bra_cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^collections/', include(collection_urls)),
)
