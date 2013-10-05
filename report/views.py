from result_generator.report.header import *
from result_generator.report.models import *
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory
from django.core.context_processors import csrf

def index(request):
	return render_to_response('index.html', context_instance = 
		RequestContext(request))
	
def new_student(request):
	if request.method == "POST":
			form = StudentForm(request.POST)
			if form.is_valid():
				form.save()	
				x = {'form': form,}
				return render_to_response('report/student_ok.html',x,
				context_instance=RequestContext(request))
	else:	
		form = StudentForm()
	x = {'form': form,}
	return render_to_response('report/student.html',x, context_instance = RequestContext(request))
		
def sel_type(request):
	clas = Class.objects.all()
	test = Tests.objects.all()
	temp = {'clas':clas,'test':test}
	return render_to_response('report/select_type.html',temp, 
	context_instance= RequestContext(request))
		
def add_result(request):
	
	clas = Class.objects.get(id=request.GET['class'])
	test = Tests.objects.get(id=request.GET['test'])
	student = Student.objects.filter(std=clas.id)
	#for students in student:
	#	student_id = Student.objects.get(id=students.id)
	if test.id == 3 or test.id == 6:
		for students in student:
			stu = Student.objects.get(id=students.id)
			if request.method == 'POST':
				form = SAtestForm(request.POST)
				if form.is_valid() :
					marks = form.save(commit=False)
					marks.test = test					
					marks.save()
					return HttpResponseRedirect(reverse('result_generator.report.views.add_result'))
			else:
				form = SAtestForm()
			temp = {'form': form, 'student':stu,'test':test }
			return render_to_response('report/add_marks.html', temp, 
			context_instance = RequestContext(request))
	else :
		for students in student:
			stu = Student.objects.get(id=students.id)
			if request.method == 'POST':
				form = FAtestForm(request.POST)
				if form.is_valid() :
					marks = form.save(commit=False)
					marks.test = test					
					marks.save()
			else:
				form = FAtestForm()
			temp = {'form': form, 'student':stu,'test':test }
			return render_to_response('report/add_marks.html', temp, 
			context_instance = RequestContext(request))
		return render_to_response('report/marks_filled.html',
		{'student':student}, context_instance=RequestContext(request))
	
		
def marks_fill(request):
	FAresult.objects.all().delete()
	fatest = FAtest.objects.all()
	for i in range(1,fatest.count()+1):
	     res = FAtest.objects.get(id =i)
	     fa_res = FAresult(fatest=res)
	     fa_res.save()
	     maxm = Maxmarks.objects.filter(test = res.test).filter(clas=res.student.std).values('id')
	     maxid = Maxmarks.objects.get(id = maxm)
	     list4 = ['a_eng','a_pun','a_sst','a_sci','a_math','a_comp','a_draw','a_m_oral']
	     #list2 = ['q_eng','q_pun','q_sst','q_sci','q_math','q_comp','q_draw','q_m_oral']
	     list1 = [res.a_eng,res.a_pun,res.a_sst,res.a_sci,res.a_math,res.a_comp,res.a_draw,res.a_m_oral]
	     list2 = [res.q_eng,res.q_pun,res.q_sst,res.q_sci,res.q_math,res.q_comp,res.q_draw,res.q_m_oral]
	     list3 = [maxid.a_eng,maxid.a_pun,maxid.a_sst,maxid.a_sci,maxid.a_math,maxid.a_comp,maxid.a_draw,maxid.a_m_oral]
	     for act,qp,act2,act3 in zip(list1,list2,list3,list4):
	     	 result = act
	     	 qpaper= qp
	     	 ran = result.split(',')
	     	 temp = [0,0,0,0,0,0,0,0,0,0]
	     	 j = 0
	     	 while j<len(ran):
	     	 	temp[j]=ran[j]
	     	 	j+=1
	     	 
	     	 maxres = act2
	     	 range_res = maxres.split(',')
	     	 temp_max = [0,0,0,0,0,0,0,0,0,0]
	     	 k = 0
	     	 while k<len(range_res):
	     	 	temp_max[k]=range_res[k]
	     	 	k+=1
	     	 amount1 = float(temp[0])*10/float(temp_max[0])
	     	 amount2 = float(temp[1])*10/float(temp_max[1])
	     	 amount3 = float(temp[2])*10/float(temp_max[2])
	     	 amount4 = float(temp[3])*10/float(temp_max[3])
	     	 amount5 = float(temp[4])*10/float(temp_max[4])
	     	 amount6 = float(temp[5])*10/float(temp_max[5])
	     	 amount7 = float(temp[6])*10/float(temp_max[6])
	     	 amount8 = float(temp[7])*10/float(temp_max[7])
	     	 amount9 = float(temp[8])*10/float(temp_max[8])
	     	 amount10 = float(temp[9])*10/float(temp_max[9])
	     	 import heapq
	     	 amountn = [amount1,amount2,amount3,amount4,amount5,amount6,amount7,amount8,amount9,amount10]
	     	 large=heapq.nlargest(3,amountn)
	     	 sum_large = sum(large)
	     	 fa_marks=round((sum_large+qpaper)*10/40,2)
	     	 fa_total=fa_marks*10
	     	 if act3=='a_eng':
	     	 	FAresult.objects.filter(fatest=res).update(max3_eng=large,marks_eng=fa_marks,total_eng=fa_total)
	     	 elif act3=='a_pun':
	     	 	FAresult.objects.filter(fatest=res).update(max3_pun=large,marks_pun=fa_marks,total_pun=fa_total)
	     	 elif act3=='a_sst':
	     	 	FAresult.objects.filter(fatest=res).update(max3_sst=large,marks_sst=fa_marks,total_sst=fa_total)
	     	 elif act3=='a_sci':
	     	 	FAresult.objects.filter(fatest=res).update(max3_sci=large,marks_sci=fa_marks,total_sci=fa_total)
	     	 elif act3=='a_math':
	     	 	FAresult.objects.filter(fatest=res).update(max3_math=large,marks_math=fa_marks,total_math=fa_total)
	     	 elif act3=='a_comp':
	     	 	FAresult.objects.filter(fatest=res).update(max3_comp=large,marks_comp=fa_marks,total_comp=fa_total)
	     	 elif act3=='a_draw':
	     	 	FAresult.objects.filter(fatest=res).update(max3_draw=large,marks_draw=fa_marks,total_draw=fa_total)
	     	 elif act3=='a_m_oral':
	     	 	FAresult.objects.filter(fatest=res).update(max3_m_oral=large,marks_m_oral=fa_marks,total_m_oral=fa_total)
	return render_to_response('report/marks_ok.html', context_instance = RequestContext(request))
	     
	    
def sa_marks_fill(request):
	SAresult.objects.all().delete()
	satest = SAtest.objects.all()
	for i in range(1,satest.count()+1):
		res = SAtest.objects.get(id =i)
		sa_res = SAresult(satest=res)
		sa_res.save()
		maxm = Maxmarks.objects.filter(test = res.test).filter(clas=res.student.std).values('id')
		maxid = Maxmarks.objects.get(id = maxm)
		list1 = [res.q_eng,res.q_pun,res.q_sst,res.q_sci,res.q_math,res.q_comp,res.q_draw,res.q_m_oral]
		list2 = [maxid.q_eng,maxid.q_pun,maxid.q_sst,maxid.q_sci,maxid.q_math,maxid.q_comp,maxid.q_draw,maxid.q_m_oral]
		list3 = ['q_eng','q_pun','q_sst','q_sci','q_math','q_comp','q_draw','q_m_oral']
		for qp,qp2,qp3 in zip(list1,list2,list3):
			sa_marks=qp*30/qp2
			sa_total=sa_marks*3.33
			if qp3=='q_eng':
				SAresult.objects.filter(satest=res).update(marks_eng=sa_marks,total_eng=sa_total)
			elif qp3=='q_pun':
				SAresult.objects.filter(satest=res).update(marks_pun=sa_marks,total_pun=sa_total)
			elif qp3=='q_sst':
				SAresult.objects.filter(satest=res).update(marks_sst=sa_marks,total_sst=sa_total)
			elif qp3=='q_sci':
				SAresult.objects.filter(satest=res).update(marks_sci=sa_marks,total_sci=sa_total)
			elif qp3=='q_math':
				SAresult.objects.filter(satest=res).update(marks_math=sa_marks,total_math=sa_total)
			elif qp3=='q_comp':
				SAresult.objects.filter(satest=res).update(marks_comp=sa_marks,total_comp=sa_total)
			elif qp3=='q_draw':
				SAresult.objects.filter(satest=res).update(marks_draw=sa_marks,total_draw=sa_total)
			elif qp3=='q_m_oral':
				SAresult.objects.filter(satest=res).update(marks_m_oral=sa_marks,total_m_oral=sa_total)
	return render_to_response('report/marks_ok.html', context_instance = RequestContext(request))
	  
	     	 	
def search(request):
	"""
	** search **
	Here's the new search.
	The function get_query is defined in funcions.py file
	"""
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['name', 'address',
		'roll_no',])
		found_entries = Student.objects.filter(entry_query).order_by('name')
        temp ={ 'query_string': query_string, 'found_entries': found_entries }
        return render_to_response('report/search_results.html',temp, 
        context_instance= RequestContext(request))
        
def add_marks(request):
	student = Student.objects.get(id=request.GET['id'])
	if request.method == "POST":
			form = AddMarksForm(request.POST)
			if form.is_valid():
				pro = form.save(commit=False)
				pro.student = student
				pro.save()
				x = {'form': form,}
				test = QAtest.objects.aggregate(Max('id'))
				max_id =test['id__max']
				marks = QAtest.objects.get(id =max_id)
				if marks.test == 3 or marks.test == 6 :
					return render_to_response('school/marks_filled.html',temp,
					context_instance=RequestContext(request))
				else:
					return HttpResponseRedirect(reverse('pps.school.views.add_activities'))
	else:	
		form = AddMarksForm()
	x = {'form': form,}
	return render_to_response('school/add_marks.html',x, context_instance = 
	RequestContext(request))
    
    
def add_activities(request):
	class RequiredFormSet(BaseFormSet):
		def __init__(self, *args, **kwargs):
			super(RequiredFormSet, self).__init__(*args, **kwargs)
			for form in self.forms:
				form.empty_permitted = False

	test = QAtest.objects.aggregate(Max('id'))
	max_id =test['id__max']
	qa = QAtest.objects.get(id =max_id)
	ActivityFormSet = formset_factory(ActivityForm, max_num=30, formset=RequiredFormSet)
	if request.method == 'POST':
		activity_formset = ActivityFormSet(request.POST, request.FILES)
		if activity_formset.is_valid():
			for form in activity_formset.forms:
				activity = form.save(commit=False)
    			activity.qa_id = qa.id
    			activity.save()
    			id = Activity.objects.aggregate(Max('id'))
    			maxid =id['id__max']
    			activity = Activity.objects.get(id=maxid)
    			max_marks = Maxmarks.objects.filter(sub=qa.subject).\
    			filter(test=qa.test).filter(clas=qa.student.std).\
    			filter(other=activity.name).values('id')
    			mmarks_id = Maxmarks.objects.get(id = max_marks)
    			
    			mark = activity.marks
    			perc_marks = mark*int(mmarks_id.perc)/int(mmarks_id.maxmarks)
    			mark = Activity.objects.filter(id =maxid).update(perc_marks=perc_marks)
    			return render_to_response('school/marks_filled.html',
    			context_instance=RequestContext(request))
	else:
		activity_formset = ActivityFormSet()
	temp = {'activity_formset': activity_formset, }
	return render_to_response('school/add_activities.html', temp, 
	context_instance = RequestContext(request))
        
def add_skills(request):
	if request.method == "POST":
			form1 = ThinkingSkillsForm(request.POST)
			form2 = SocialSkillsForm(request.POST)
			form3 = EmotionalSkillsForm(request.POST)
			if form1.is_valid and form2.is_valid() and form3.is_valid():
				form1.save()
				form2.save()		
				form3.save()
				return render_to_response('report/student_ok.html',
				context_instance=RequestContext(request))
	else:	
		form1 = ThinkingSkillsForm()
		form2 = SocialSkillsForm()
		form3 = EmotionalSkillsForm()
	x = {'form1': form1,'form2':form2,'form3':form3}
	return render_to_response('report/skills.html',x, context_instance = RequestContext(request))

