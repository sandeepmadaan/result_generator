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
		exclude= ['test',]
	
	
class FAresult(models.Model):
	fatest = models.OneToOneField(FAtest)
	max3_eng = models.CharField(max_length=20,blank=True,null=True)
	marks_eng = models.FloatField(blank=True,null=True)
	total_eng = models.FloatField(blank=True,null=True)
	max3_pun = models.CharField(max_length=20,blank=True,null=True)
	marks_pun = models.FloatField(blank=True,null=True)
	total_pun = models.FloatField(blank=True,null=True)
	max3_sst = models.CharField(max_length=20,blank=True,null=True)
	marks_sst = models.FloatField(blank=True,null=True)
	total_sst = models.FloatField(blank=True,null=True)
	max3_sci = models.CharField(max_length=20,blank=True,null=True)
	marks_sci = models.FloatField(blank=True,null=True)
	total_sci = models.FloatField(blank=True,null=True)
	max3_math = models.CharField(max_length=20,blank=True,null=True)
	marks_math = models.FloatField(blank=True,null=True)
	total_math = models.FloatField(blank=True,null=True)
	max3_comp = models.CharField(max_length=20,blank=True,null=True)
	marks_comp = models.FloatField(blank=True,null=True)
	total_comp = models.FloatField(blank=True,null=True)
	max3_draw = models.CharField(max_length=20,blank=True,null=True)
	marks_draw = models.FloatField(blank=True,null=True)
	total_draw = models.FloatField(blank=True,null=True)
	max3_m_oral = models.CharField(max_length=20,blank=True,null=True)
	marks_m_oral = models.FloatField(blank=True,null=True)
	total_m_oral = models.FloatField(blank=True,null=True)
	
class SAtest(models.Model):
	student = models.ForeignKey(Student)
	test = models.ForeignKey(Tests)
	q_eng = models.FloatField(default="0.0")
	q_pun = models.FloatField(default="0.0")
	q_sst = models.FloatField(default="0.0")
	q_sci = models.FloatField(default="0.0")
	q_math = models.FloatField(default="0.0")
	q_comp = models.FloatField(default="0.0")
	q_draw = models.FloatField(default="0.0")
	q_m_oral = models.FloatField(default="0.0")
	
class SAtestForm(ModelForm):
	class Meta :
		model = SAtest
		exclude= ['test',]

class SAresult(models.Model):
	fatest = models.OneToOneField(SAtest)
	marks_eng = models.FloatField(blank=True,null=True)
	total_eng = models.FloatField(blank=True,null=True)
	marks_pun = models.FloatField(blank=True,null=True)
	total_pun = models.FloatField(blank=True,null=True)
	marks_sst = models.FloatField(blank=True,null=True)
	total_sst = models.FloatField(blank=True,null=True)
	marks_sci = models.FloatField(blank=True,null=True)
	total_sci = models.FloatField(blank=True,null=True)
	marks_math = models.FloatField(blank=True,null=True)
	total_math = models.FloatField(blank=True,null=True)
	marks_comp = models.FloatField(blank=True,null=True)
	total_comp = models.FloatField(blank=True,null=True)
	marks_draw = models.FloatField(blank=True,null=True)
	total_draw = models.FloatField(blank=True,null=True)
	marks_m_oral = models.FloatField(blank=True,null=True)
	total_m_oral = models.FloatField(blank=True,null=True)
	
class ThinkingSkills(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2  = models.FloatField(default="0.0")
	skill3  = models.FloatField(default="0.0")
	skill4  = models.FloatField(default="0.0")
	skill5  = models.FloatField(default="0.0")
	skill6  =  models.FloatField(default="0.0")
	skill7  = models.FloatField(default="0.0")
	skill8  = models.FloatField(default="0.0")
	skill9  = models.FloatField(default="0.0")
	skill10  = models.FloatField(default="0.0")
	
class ThinkingSkillsForm(ModelForm):
	
	class Meta :
		model = ThinkingSkills
		
	skill1 = forms.FloatField(label='Knows his or her strengths and weaknesses')
	skill2 = forms.FloatField(label='Demonstrates internal or external locus of control')
	skill3 = forms.FloatField(label='Knows his or her way of dealing with people events and things')
	skill4 = forms.FloatField(label='Recognizes and analyzes a problem')
	skill5 = forms.FloatField(label='Collects relevant information from reliable sources')
	skill6 = forms.FloatField(label='Evaluates each alternative for advantageous and adverse consequences of each alternative situation')
	skill7 = forms.FloatField(label='Chooses the best alternative shows originality and innovation')
	skill8 = forms.FloatField(label='Demonstrates fluency in ideas get lots of new ideas')
	skill9 = forms.FloatField(label='Open to modification and flexibility in thinking')
	skill10 = forms.FloatField(label='Demonstrates divergent thinking')
		
class SocialSkills(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class SocialSkillsForm(ModelForm):
	
	class Meta :
		model = SocialSkills
		
	skill1 = forms.FloatField(label='Helps classmates in case of difficulties in academic and personal issues')
	skill2 = forms.FloatField(label='Seeks feedback from teachers and peers for self improvement')
	skill3 = forms.FloatField(label='Actively listens and pays attention of others when speaking in the class school assembly and other occasions')
	skill4 = forms.FloatField(label='Sees and appreciates others point of view')
	skill5 = forms.FloatField(label='Draws attention of others when speaking in the class school assembly and other occasions')
	skill6 = forms.FloatField(label='Explains and articulates a concept differently so that others can understand in simple language')
	skill7 = forms.FloatField(label='Sensitive to the needs of differently abled students')
	skill8 = forms.FloatField(label='Demonstates leadership skills like responsibility initiative etc')
	skill9 = forms.FloatField(label='Demonstrates awareness of norms and social conduct and follows them')
	skill10 = forms.FloatField(label='Helps develop skills and competencies in others instead of makingthem dependent')

class EmotionalSkills(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class EmotionalSkillsForm(ModelForm):
	
	class Meta :
		model = EmotionalSkills
		
	skill1 = forms.FloatField(label='Is optimistic')
	skill2 = forms.FloatField(label='Believes in self confidence and thinks "I can "')
	skill3 = forms.FloatField(label='Manages Scholastic, Co-Scholastic and personal challenges')
	skill4 = forms.FloatField(label='If unsuccessful, gracefully takes the task again')
	skill5 = forms.FloatField(label='Seeks help of teachers and classmates in difficult situations')
	skill6 = forms.FloatField(label='Does not get into unhealthy habits when under stress')
	skill7 = forms.FloatField(label='Maintains decency under stressful interpersonal situations')
	skill8 = forms.FloatField(label='Expresses feelings and reactions frankly in the class')
	skill9 = forms.FloatField(label='Supports and empathises with others')
	skill10 = forms.FloatField(label='Politely declines - "say no", when he/she does not want to undertake a task')
	
class WorkEducation(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class WorkEducationForm(ModelForm):
	
	class Meta :
		model = WorkEducation
		
	skill1 = forms.FloatField(label='Has a collaborative approach towards the process of learning')
	skill2 = forms.FloatField(label='Is Innovative in ideas')
	skill3 = forms.FloatField(label='Plans and adheres to timelines')
	skill4 = forms.FloatField(label='Is Involved and motivated')
	skill5 = forms.FloatField(label='Demonstrates a positive atitude')
	skill6 = forms.FloatField(label='Is helpful,guides and facilitates others')
	skill7 = forms.FloatField(label='Demonstrates an understanding of correlation with real life situation')
	skill8 = forms.FloatField(label='Has a step-by-step approach to solving a problem')
	skill9 = forms.FloatField(label='Has clear understanding of output to be generated')
	skill10 = forms.FloatField(label='Is able to apply the theoretical knowledge into practical usage')
	
class VisualArts(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class VisualArtForm(ModelForm):
	
	class Meta :
		model = Visual Arts 
		
	skill1 = forms.FloatField(label='Takes an innivative and creative approach')
	skill2 = forms.FloatField(label='Shows aesthetic sensibilities')
	skill3 = forms.FloatField(label='Displays observation skills')
	skill4 = forms.FloatField(label='Demonstrates interpretation and originality')
	skill5 = forms.FloatField(label='Corelates with real life')
	skill6 = forms.FloatField(label='Shows willingness to experiment with different art modes/mediums')
	skill7 = forms.FloatField(label='sketches or paints')
	skill8 = forms.FloatField(label='Generates computer application')
	skill9 = forms.FloatField(label='Demonstrates proportion in size and clarity')
	skill10 = forms.FloatField(label='Understand the importance of colour, balance and brightness')
	
	
class PerformingArts(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class PerformingArtsForm(ModelForm):
	
	class Meta :
		model = PerformingArts 
		
	skill1 = forms.FloatField(label='Sings and plays instrumental music')
	skill2 = forms.FloatField(label='Dances and acts in drama')
	skill3 = forms.FloatField(label='Awarness and appreciation of works of artists')
	skill4 = forms.FloatField(label='Demonstrates appreciation skills')
	skill5 = forms.FloatField(label='Participates actively in aesthetic activities at various levels')
	skill6 = forms.FloatField(label='Takes initiative to plan , create and direct various creative events')
	skill7 = forms.FloatField(label='Roads and shows a degree of awarness of particular of domain of art')
	skill8 = forms.FloatField(label='Experiments with art forms')
	skill9 = forms.FloatField(label='Shows a high degree of imagination and innovation')
	skill10 = forms.FloatField(label='Displays artistic temperament in all of his/her actions i school and outside')
	
	
class AttitudeToTeachers(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class AttitudeToTeachersForm(ModelForm):
	
	class Meta :
		model = AttitudeToTeachers
		
	skill1 = forms.FloatField(label='Shows decency and courtesy to teachers inside and outside the class')
	skill2 = forms.FloatField(label='Demonstrates positive atitudes towards learning')
	skill3 = forms.FloatField(label='Takes suggestions and criticism in the right spirit ')
	skill4 = forms.FloatField(label='Respects teachers instructions')
	skill5 = forms.FloatField(label='Accepts norms and rules of the school')
	skill6 = forms.FloatField(label='Communicates his/her thoughts with teachers')
	skill7 = forms.FloatField(label='Confides his/her problems with the teachers')
	skill8 = forms.FloatField(label='Shows honesty and sincerity towards teachers')
	skill9 = forms.FloatField(label='Feels free to ask questions')
	skill10 = forms.FloatField(label='Helpful to teachers')
	
class AttitudeToMates(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class AttitudeToMatesForm(ModelForm):
	
	class Meta :
		model = AttitudeToMates
		
	skill1 = forms.FloatField(label='Is friendly with most of the classmates')
	skill2 = forms.FloatField(label='Expresses ideas and opinions freely in a group')
	skill3 = forms.FloatField(label='Is receptive to ideas and opinion of others')
	skill4 = forms.FloatField(label='Treats classmates as equals, without any sense of superiority or inferiority')
	skill5 = forms.FloatField(label='Sensitive and supportive towards peers and differently-abled school-mates')
	skill6 = forms.FloatField(label='Treats peers from different social, religious and economic background without any discrimination')
	skill7 = forms.FloatField(label='Respects opposite gender and is comfortable in their company')
	skill8 = forms.FloatField(label='Does not bully others')
	skill9 = forms.FloatField(label='Deals factfully with the peers having aggressive behaviour')
	skill10 = forms.FloatField(label='Shares credit and praise with team members and peers')
	
class AtitudeToEnv(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
class AtitudeToEnvForm(ModelForm)
	
	class Meta :
		model = AtitudeToEnv
		
	skill1 = forms.FloatField(label='Attaches a lot of importance to school activities and programmes')
	skill2 = forms.FloatField(label='Participates in school activities relating to improvement of environment')
	skill3 = forms.FloatField(label='Enithusiastically participates in school programmes')
	skill4 = forms.FloatField(label='Shoulders responsibility happily')
	skill5 = forms.FloatField(label='Confronts any one who criticises school and school programmes')
	skill6 = forms.FloatField(label='Insists on parents to participate / witness school programmes')
	skill7 = forms.FloatField(label='Participates in community activities relating to environment')
	skill8 = forms.FloatField(label='Takes care of school property')
	skill9 = forms.FloatField(label='Sensitive and concerned about environmental degradation')
	skill10 = forms.FloatField(label='Takes initiative in planning activities for the betterment of environment')
	
class EmotionalSkills(models.Model):
	student = models.ForeignKey(Student)
	skill1 = models.FloatField(default="0.0")
	skill2 = models.FloatField(default="0.0")
	skill3 = models.FloatField(default="0.0")
	skill4 = models.FloatField(default="0.0")
	skill5 = models.FloatField(default="0.0")
	skill6 = models.FloatField(default="0.0")
	skill7 = models.FloatField(default="0.0")
	skill8 = models.FloatField(default="0.0")
	skill9 = models.FloatField(default="0.0")
	skill10 = models.FloatField(default="0.0")
	
"""		
class ThinkingSkills(models.Model):
	knows his or her strengths and weaknesses = models.FloatField(default="0.0")
	demonstrates internal or external locus of control = models.FloatField(default="0.0")
	knows his or her way of dealing with people events and things = models.FloatField(default="0.0")
	recognizes and analyzes a problem = models.FloatField(default="0.0")
	collects relevant information from reliable sources = models.FloatField(default="0.0")
	evaluates each alternative for advantageous and adverse consequences of each alternative situation =  models.FloatField(default="0.0")
	chooses the best alternative shows originality and innovation = models.FloatField(default="0.0")
	demonstrates fluency in ideas get lots of new ideas = models.FloatField(default="0.0")
	open to modification and flexibility in thinking = models.FloatField(default="0.0")
	demonstrates divergent thinking = models.FloatField(default="0.0")
	

class SocialSkills(models.Model):
	helps classmateS in case of difficulties in academic and personal issues = models.FloatField(default="0.0")
	seeks feedback from teachers and peers for self improvement = models.FloatField(default="0.0")
	actively listens and pays attention of others when speaking in the class school assembly and other occasions = models.FloatField(default="0.0")
	sees and appreciates others point of view = models.FloatField(default="0.0")
	draws attention of others when speaking in the class school assembly and other occasions = models.FloatField(default="0.0")
	explains and articulates a concept differently so that others can understand in simple language = models.FloatField(default="0.0")
	sensitive to the needs of differently abled students = models.FloatField(default="0.0")
	demonstates leadership skills like responsibility initiative etc = models.FloatField(default="0.0")
	demonstrates awareness of norms and social conduct and follows them = models.FloatField(default="0.0")
	helps develop skills and competencies in others instead of makingthem dependent = models.FloatField(default="0.0")
	"""
