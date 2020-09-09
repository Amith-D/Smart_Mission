from django import forms
from . import models
from basicapp.models import Student
class AdmitStudent(forms.ModelForm):
	class Meta:
		model = models.Student
		fields = ['First_Name','Last_Name','Email', 'Gender', 
		'Tenth_Board', 'Tenth_Medium','Tenth_Math','Tenth_Science', 
		'Tenth_Eng','Tenth_Total','Twelth_Math','Twelth_Physics',
		'Twelth_Chemistry','Twelth_Optional','Twelth_Eng','Twelth_Total',
		'Twelth_Board','English_Profieciency', 'CET_or_Comedk',
		'Extra_curricular_participation','Extra_curricular_activity',
		'Level_of_achievement','Father_Qualification','Mother_Qualification',
		'Annual_family_income','Did_you_migrate_frome_hometown',
		'Distance_between_school_or_college_and_home','How_do_describe_yourself_as',
		'Do_you_take_initiative_in_a_work','Are_you_a_procrastinator',
		'Logical_reasoning','Interested_in_research','Are_you_open_to_a_relationships',
		'Was_joining_engineering_your_personnel_choice']
		widgets = {
			'First_Name':forms.TextInput(attrs={'class':'form-control'}),
			'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
			'Email':forms.EmailInput(attrs={'class':'form-control'}),
			'Gender':forms.Select(attrs={'class':'form-control'}),
			'Tenth_Board':forms.Select(attrs={'class':'form-control'}),
			'Tenth_Medium':forms.Select(attrs={'class':'form-control'}),
			'Tenth_Math':forms.NumberInput(attrs={'class':'form-control'}),
			'Tenth_Science':forms.NumberInput(attrs={'class':'form-control'}),
			'Tenth_Eng':forms.NumberInput(attrs={'class':'form-control'}),
			'Tenth_Total':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Math':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Physics':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Chemistry':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Optional':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Eng':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Total':forms.NumberInput(attrs={'class':'form-control'}),
			'Twelth_Board':forms.Select(attrs={'class':'form-control'}),
			'English_Profieciency':forms.Select(attrs={'class':'form-control'}),
			'CET_or_Comedk':forms.NumberInput(attrs={'class':'form-control'}),
			'Extra_curricular_participation':forms.Select(attrs={'class':'form-control'}),
			'Extra_curricular_activity':forms.TextInput(attrs={'class':'form-control'}),
			'Level_of_achievement':forms.Select(attrs={'class':'form-control'}),
			'Father_Qualification':forms.Select(attrs={'class':'form-control'}),
			'Mother_Qualification':forms.Select(attrs={'class':'form-control'}),
			'Annual_family_income':forms.Select(attrs={'class':'form-control'}),
			'Did_you_migrate_frome_hometown':forms.Select(attrs={'class':'form-control'}),
			'Distance_between_school_or_college_and_home':forms.NumberInput(attrs={'class':'form-control'}),
			'How_do_describe_yourself_as':forms.Select(attrs={'class':'form-control'}),
			'Do_you_take_initiative_in_a_work':forms.Select(attrs={'class':'form-control'}),
			'Are_you_a_procrastinator':forms.Select(attrs={'class':'form-control'}),
			'Logical_reasoning':forms.Select(attrs={'class':'form-control'}),
			'Interested_in_research':forms.Select(attrs={'class':'form-control'}),
			'Are_you_open_to_a_relationships':forms.Select(attrs={'class':'form-control'}),
			'Was_joining_engineering_your_personnel_choice':forms.Select(attrs={'class':'form-control'})

		}


			
				

			
		
