"""
%% urls.py %%

This file define the urls used in the software for tcc application. In this regular expression are used, which are used to connect the url with the functions defined.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.conf.urls.defaults import *
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()
from result_generator.report.models import *
from result_generator.report.views import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE URLS HERE::::::::::::::::::::::::::::::::::::#

urlpatterns = patterns('result_generator.report.views',
	(r'^newstudent/$', 'new_student'),
	(r'^search/$', 'search'),
	(r'^addmarks/$', 'add_marks'),
	(r'^add_activities/$', 'add_activities'),
	(r'^seltype/$', 'sel_type'),
	(r'^addresult/$', 'add_result'),
	(r'^gen_res/$', 'marks_fill'),
	(r'^add_skills/$', 'add_skills'),
   #(r'^publishers/$', PublisherDetail.as_view()),
)


