"""
%% urls.py %%

This file is define the main url for the Software. It links the software with different applications.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE URLS HERE::::::::::::::::::::::::::::::::::::#


urlpatterns = patterns('',
    (r'^$', 'result_generator.report.views.index'),
	(r'^report/', include('result_generator.report.urls')),
    (r'^admin/', include(admin.site.urls)),
   
)

