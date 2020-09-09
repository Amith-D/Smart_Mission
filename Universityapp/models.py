from django.db import models

# Create your models here.
class student_data(models.Model):
    GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
    )

    MEDIUM_CHOICES = (
		('1', 'English'),
		('2', 'Kannada')
    )

    BOARD_CHOICES = (
        ('1', 'STATE'),
        ('2', 'CBSE'),
        ('3', 'ICSE')
    )

    PROFICIENCY_CHOICES = (
        ('1','BEGINNER'),
        ('2','INTERMEDIATE'),
        ('3','NATIVE SPEAKER')
    )

    YES_NO_CHOICES = (
        ('1','NO'),
        ('1.5','Maybe'),
        ('2','YES')
    )

    ACHIEVEMENT_CHOICES = (
        ('1','SCHOOL LEVEL'),
        ('2', 'COLLEGE LEVEL'),
        ('3', 'NATIONAL LEVEL'),
        ('4', 'INTERNATIONAL LEVEL')
    )

    QUALIFICATION_CHOICES = (
        ('1','BELOW TENTH'),
        ('2', 'TENTH'),
        ('3', 'BACHELORS'),
        ('4', 'MASTERS'),
        ('5', 'PHD')

    )

    INCOME_CHOICES = (
        ('1','BELOW 1 LAKH'),
        ('2', '1L-2L'),
        ('3', '2L-4L'),
        ('4', '4L-6L'),
        ('5', 'Above 6 lakh')

    )

    DESCRIBE_CHOICES = (
        ('1','Introvert'),
        ('1.5','Extrovert'),
        ('2','Ambivert')
    )

    LOGIC_RATING = (
        ('1', '1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )


    University = models.CharField(max_length=264, unique = True, null = True)
    Email = models.CharField(max_length= 200,  null = True)
    First_Name = models.CharField(max_length= 200,  null = True)
    Last_Name = models.CharField(max_length= 200,  null = True)
    USN = models.CharField(max_length=200, null = True)
    Gender=models.CharField(max_length=15, choices=GENDER_CHOICES, null = True)
    Tenth_Board = models.FloatField(choices = BOARD_CHOICES, null = True)
    Tenth_Medium = models.FloatField(choices=MEDIUM_CHOICES, null = True)
    Tenth_Math = models.FloatField(null = True)
    Tenth_Science = models.FloatField(null = True)
    Tenth_Eng = models.FloatField(null = True)
    Tenth_Total = models.FloatField(null = True)
    Twelth_Math = models.FloatField(null = True)
    Twelth_Physics = models.FloatField(null = True)
    Twelth_Chemistry = models.FloatField(null = True)
    Twelth_Optional = models.FloatField(null = True)
    Twelth_Eng = models.FloatField(null = True)
    Twelth_Total = models.FloatField(null = True)
    Twelth_Board = models.FloatField( choices = BOARD_CHOICES, null = True)
    English_Profieciency =  models.IntegerField( choices = PROFICIENCY_CHOICES, null = True)
    CETorComedk = models.IntegerField(null = True)
    Extra_curricular_participation =  models.FloatField(choices = YES_NO_CHOICES, null = True)
    Extra_curricular_activity = models.CharField(max_length= 200, null = True)
    Levelof_achievement = models.IntegerField( choices = ACHIEVEMENT_CHOICES, null = True)
    FatherQualification =  models.IntegerField(choices = QUALIFICATION_CHOICES, null = True)
    MotherQualification =  models.IntegerField(choices = QUALIFICATION_CHOICES, null = True)
    FamilyIncome =  models.IntegerField(choices = INCOME_CHOICES, null = True)
    Are_you_a_migrate = models.FloatField(choices = YES_NO_CHOICES, null = True)
    Distance = models.FloatField(null = True)
    Branch = models.CharField(max_length= 200, null = True)
    First_Sem = models.FloatField(null = True)
    Second_Sem = models.FloatField(null = True )
    Third_Sem = models.FloatField(null = True)
    Fourth_Sem = models.FloatField(null = True)
    Fifth_Sem = models.FloatField(null = True)
    Sixth_Sem = models.FloatField(null = True)
    Seventh_Sem = models.FloatField(null = True)
    Eight_Sem = models.FloatField(null = True)
    CGPA = models.FloatField(null = True)
    Extra_activity = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Specify_extraactivity = models.CharField( max_length=500, null = True)
    What_level_of_participation = models.IntegerField(null = True, choices = ACHIEVEMENT_CHOICES)
    Can_you_handle_a_professional_team = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Are_you_a_team_player = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Have_you_worked_in_the_same_field = models.FloatField(null = True, choices = YES_NO_CHOICES)
    How_do_describe_yourself_as = models.IntegerField(null = True, choices = DESCRIBE_CHOICES)
    Do_you_take_initiative_in_a_work = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Are_you_a_procrastinator = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Logical_reasoning =  models.IntegerField(null = True, choices = LOGIC_RATING)
    Have_you_been_in_any_research = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Internship = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Company_demand = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Relationships = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Personnel_choice = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Campus_recruid = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Higher_education = models.FloatField(null = True, choices = YES_NO_CHOICES)
    Package =  models.FloatField(null = True)
    joinyear = models.IntegerField(null = True)

    def __str__(self):
        return '%s %s %s'%(self.First_Name, self.Last_Name, self.University)
