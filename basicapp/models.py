from django.db import models
from datetime import date
# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
		('1', 'Male'),
		('2', 'Female')
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
    Time = models.DateTimeField(default=date.today,editable=False, null=False, blank=False)
    First_Name = models.CharField(max_length=100,null = True)
    Last_Name = models.CharField(max_length=100,null = True)
    Email = models.EmailField(max_length=100, null = True)
    Gender = models.CharField(max_length=15, choices=GENDER_CHOICES, null = True)
    Tenth_Board = models.CharField(max_length=2, choices = BOARD_CHOICES, null = True)
    Tenth_Medium = models.CharField(max_length=15, choices=MEDIUM_CHOICES, null = True)
    Tenth_Math = models.IntegerField(null = True)
    Tenth_Science = models.IntegerField(null = True)
    Tenth_Eng = models.IntegerField(null = True)
    Tenth_Total = models.IntegerField(null = True)
    Twelth_Math = models.IntegerField(null = True)
    Twelth_Physics = models.IntegerField(null = True)
    Twelth_Chemistry = models.IntegerField(null = True)
    Twelth_Optional = models.IntegerField(null = True)
    Twelth_Eng = models.IntegerField(null = True)
    Twelth_Total = models.IntegerField(null = True)
    Twelth_Board = models.CharField(max_length= 20,choices = BOARD_CHOICES,null = True)
    English_Profieciency =  models.CharField(null = True,max_length= 20,choices =  PROFICIENCY_CHOICES)
    CET_or_Comedk = models.IntegerField(null = True)
    Extra_curricular_participation =  models.CharField(null = True,max_length= 20,choices = YES_NO_CHOICES )
    Extra_curricular_activity = models.CharField(null = True,max_length=250)
    Level_of_achievement = models.CharField(null = True,max_length= 20,choices = ACHIEVEMENT_CHOICES )
    Father_Qualification =  models.CharField(null = True,max_length= 20,choices = QUALIFICATION_CHOICES)
    Mother_Qualification =  models.CharField(null = True,max_length= 20,choices = QUALIFICATION_CHOICES)
    Annual_family_income = models.CharField(max_length= 20,choices = INCOME_CHOICES ,null=True )
    Did_you_migrate_frome_hometown = models.CharField(null = True,max_length= 20,choices = YES_NO_CHOICES)
    Distance_between_school_or_college_and_home = models.IntegerField(null = True)
    How_do_describe_yourself_as = models.CharField(null = True,max_length= 20,choices = DESCRIBE_CHOICES )
    Do_you_take_initiative_in_a_work = models.CharField(null = True,max_length= 20,choices = YES_NO_CHOICES)
    Are_you_a_procrastinator = models.CharField(max_length= 20,choices= YES_NO_CHOICES ,null=True)
    Logical_reasoning =  models.CharField(null = True,max_length= 20,choices = LOGIC_RATING)
    Are_you_open_to_a_relationships = models.CharField(null = True,max_length= 20,choices = YES_NO_CHOICES)
    Interested_in_research = models.CharField(null = True,max_length= 20,choices = YES_NO_CHOICES)
    Was_joining_engineering_your_personnel_choice = models.CharField(null = True,max_length= 20,choices = YES_NO_CHOICES)
    I_sem = models.FloatField(null = True,blank=True)
    II_sem = models.FloatField(null = True,blank=True)
    III_sem = models.FloatField(null = True,blank=True)
    IV_sem = models.FloatField(null = True,blank=True)
    V_sem = models.FloatField(null = True,blank=True)
    VI_sem = models.FloatField(null = True,blank=True)
    VII_sem = models.FloatField(null = True,blank=True)
    VIII_sem = models.FloatField(null = True,blank=True)
    pred_avg_marks = models.FloatField(null = True,blank=True)
    pred_cocur = models.FloatField(null = True,blank=True)
    pred_intern= models.FloatField(null = True,blank=True)
    pred_pack = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.First_Name
    class Meta:
        db_table="basicapp_student"