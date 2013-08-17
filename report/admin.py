"""
%% admin.py %%

This file display usage information that admin requires to edit or add
in database tables, classes, forms and mappers in admin interface. This
make the data entry easy as one need to do it through MySQL server.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.contrib import admin
from result_generator.report.models import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE ADMIN CLASSES HERE:::::::::::::::::::::::::::#

class StudentAdmin(admin.ModelAdmin):
    	"""
	** JobAdmin **
	
	Job Admin is required to add, edit or delete the content into the Job model directly. The list to be displayed after adding and search 		and list filter	are also there.
	"""

	list_display = ('name', 'father_name','mother_name','roll_no','address','phone_no' )
	search_fields = ('name',)
	list_filter = ['name']

class SubjectsAdmin(admin.ModelAdmin):
	"""
	** ClientAdmin **
	
	Client Admin is used to add, edit or delete the client and its inforamtion directly by the admin.
	"""

	list_display = ('name',  )
	search_fields = ('name',)
	list_filter = ['name']

class TestsAdmin(admin.ModelAdmin):
	"""
	** LabAdmin **
	
	Lab Admin is used to add, edit or delete the Labs and there inforamtion directly by the admin.
	"""

	list_display = ('name', )
	search_fields = ('name',)
	list_filter = ['name']
	
class OrganisationAdmin(admin.ModelAdmin):
	"""
	** OrganisationAdmin **
	
	Organisation Admin is used to add, edit or delete the organisation 
	and its information directly by the admin.
	"""
	list_display = ('name','address', 'phone','director')
	search_fields = ('name',)
	list_filter = ['name']

class ClassAdmin(admin.ModelAdmin):
	list_display = ('name', )
	search_fields = ('name',)
	list_filter = ['name']
	
class MaxmarksAdmin(admin.ModelAdmin):
	list_display = ('test','clas','q_eng','a_eng','q_pun','a_pun','q_sst','a_sst','q_sci','a_sci','q_math',
	'a_math','q_comp','a_comp','q_draw','a_draw','q_m_oral','a_m_oral' )
	search_fields = ('test',)
	list_filter = ['test']

class FAtestAdmin(admin.ModelAdmin):
	list_display = ('test','student','q_eng','a_eng','q_pun','a_pun','q_sst','a_sst','q_sci','a_sci','q_math',
	'a_math','q_comp','a_comp','q_draw','a_draw','q_m_oral','a_m_oral' )
	search_fields = ('test',)
	list_filter = ['test']
	
class SAtestAdmin(admin.ModelAdmin):
	list_display = ('test','student','q_eng','q_pun','q_sst','q_sci','q_math',
	'q_comp','q_draw','q_m_oral', )
	search_fields = ('test',)
	list_filter = ['test']

admin.site.register(Student, StudentAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Tests, TestsAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Maxmarks, MaxmarksAdmin)
admin.site.register(FAtest, FAtestAdmin)
admin.site.register(SAtest, SAtestAdmin)
