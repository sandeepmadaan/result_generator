"""
%% models.py %%
This file contains all the defination for models of Auto software. 
including tables, classes, forms and mappers.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE:::::::::::::::::::::::::::::#
from result_generator.report.header import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#::::::::::::::::::::::DEFINE THE MODELS HERE:::::::::::::::::::::::::::#
class Organisation(models.Model):
	"""
	** Organisation **
	
	Organisation Class define all fields required to submit detail 
	about Organisation.
	
	""" 
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=20)
	director = models.CharField(max_length=50) 
	status = models.CharField(max_length=5000)
	logo_upload = models.ImageField(upload_to='logo')

	def __unicode__(self):
        	return self.name
    
class Class(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
        	return self.name
        	    	
class Student(models.Model):
	
	name = models.CharField(max_length=200)
	std = models.ForeignKey(Class)
	reg_no = models.IntegerField()
	roll_no = models.IntegerField()
	father_name = models.CharField(max_length=200)
	mother_name = models.CharField(max_length=200)
	address = models.CharField(max_length=1000)
	dob = models.CharField(max_length=200)
	phone_no = models.CharField(max_length=200)
	
	def __unicode__(self):
        	return self.name
        	
class StudentForm(ModelForm):
	
	class Meta :
		model = Student
	
	widgets = {
		'name' : TextInput(attrs={'size':60}),
		'std' : TextInput(attrs={'size':60}),
		'reg no.' : TextInput(attrs={'size':60}),
		'address' : TextInput(attrs={'size':60}),
		'roll_no' : TextInput(attrs={'size':60}),
		'father_name' : TextInput(attrs={'size':60}),
		'mother_name' : TextInput(attrs={'size':60}),
		'dob' : TextInput(attrs={'size':60}),
		'phone_no' : TextInput(attrs={'size':60}),
		
                  }

class Subjects(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
        	return self.name


class Tests(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
        	return self.name
	

class Maxmarks(models.Model):
	test = models.ForeignKey(Tests)
	clas = models.ForeignKey(Class)
	q_eng = models.IntegerField()
	a_eng = models.CharField(max_length=200)
	q_pun = models.IntegerField()
	a_pun = models.CharField(max_length=200)
	q_sst = models.IntegerField()
	a_sst = models.CharField(max_length=200)
	q_sci = models.IntegerField()
	a_sci = models.CharField(max_length=200)
	q_math = models.IntegerField()
	a_math = models.CharField(max_length=200)
	q_comp = models.IntegerField()
	a_comp = models.CharField(max_length=200)
	q_draw = models.IntegerField()
	a_draw = models.CharField(max_length=200)
	q_m_oral = models.IntegerField()
	a_m_oral = models.CharField(max_length=200)
	
class FAtest(models.Model):
	student = models.ForeignKey(Student)
	test = models.ForeignKey(Tests)
	q_eng = models.FloatField(default="0.0")
	a_eng = models.CharField(max_length=200,default="0,0,0,0,0")
	q_pun = models.FloatField(default="0.0")
	a_pun = models.CharField(max_length=200,default="0,0,0,0,0")
	q_sst = models.FloatField(default="0.0")
	a_sst = models.CharField(max_length=200,default="0,0,0,0,0")
	q_sci = models.FloatField(default="0.0")
	a_sci = models.CharField(max_length=200,default="0,0,0,0,0")
	q_math = models.FloatField(default="0.0")
	a_math = models.CharField(max_length=200,default="0,0,0,0,0")
	q_comp = models.FloatField(default="0.0")
	a_comp = models.CharField(max_length=200,default="0,0,0,0,0")
	q_draw = models.FloatField(default="0.0")
	a_draw = models.CharField(max_length=200,default="0,0,0,0,0")
	q_m_oral = models.FloatField(default="0.0")
	a_m_oral = models.CharField(max_length=200,default="0,0,0,0,0")

class FAtestForm(ModelForm):
	class Meta :
		model = FAtest
		exclude= ['test']
	
class FAresult(models.Model):
	fatest = models.OneToOneField(FAtest)
	max3_eng = models.FloatField(blank=True,null=True)
	marks_eng = models.FloatField(blank=True,null=True)
	total_eng = models.FloatField(blank=True,null=True)
	max3_pun = models.FloatField(blank=True,null=True)
	marks_pun = models.FloatField(blank=True,null=True)
	total_pun = models.FloatField(blank=True,null=True)
	max3_sst = models.FloatField(blank=True,null=True)
	marks_sst = models.FloatField(blank=True,null=True)
	total_sst = models.FloatField(blank=True,null=True)
	max3_sci = models.FloatField(blank=True,null=True)
	marks_sci = models.FloatField(blank=True,null=True)
	total_sci = models.FloatField(blank=True,null=True)
	max3_math = models.FloatField(blank=True,null=True)
	marks_math = models.FloatField(blank=True,null=True)
	total_math = models.FloatField(blank=True,null=True)
	max3_comp = models.FloatField(blank=True,null=True)
	marks_comp = models.FloatField(blank=True,null=True)
	total_comp = models.FloatField(blank=True,null=True)
	max3_draw = models.FloatField(blank=True,null=True)
	marks_draw = models.FloatField(blank=True,null=True)
	total_draw = models.FloatField(blank=True,null=True)
	max3_m_oral = models.FloatField(blank=True,null=True)
	marks_m_oral = models.FloatField(blank=True,null=True)
	total_m_oral = models.FloatField(blank=True,null=True)
	
class SAtest(models.Model):
	student = models.ForeignKey(Student)
	test = models.ForeignKey(Tests)
	q_eng = models.IntegerField()
	q_pun = models.IntegerField()
	q_sst = models.IntegerField()
	q_sci = models.IntegerField()
	q_math = models.IntegerField()
	q_comp = models.IntegerField()
	q_draw = models.IntegerField()
	q_m_oral = models.IntegerField()
	
	

		