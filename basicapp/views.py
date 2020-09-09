from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404,redirect
from basicapp.models import Student
from Universityapp.models import student_data as sd
from basicapp import forms
from basicapp.serializer import StudentSerializers
import pickle
#import sklearn.external.joblib as extjoblib
import joblib

import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.db.models.aggregates import Max
from django.db.models import Q,Avg,F
from datetime import date,datetime
from django.db.models import FloatField, Value
def index(request):
    return render(request, 'basicapp/index.html')


def AdmitStudent_view(request):
    form = forms.AdmitStudent()
    if request.method == 'POST':
        form = forms.AdmitStudent(request.POST)
        print("I'm here")
        if form.is_valid():

            np_array= list()
            print("entering validation")
            npp_array = form.cleaned_data
            if Student.objects.filter(Email=npp_array['Email']).exists():
                    print('Same')
            else:
                form.save()
            print(npp_array)
            s=['First_Name','Last_Name','Email','CET_or_Comedk','Extra_curricular_activity','Tenth_Total','Twelth_Total','Do_you_take_initiative_in_a_work','Interested_in_research' ]
            for i in npp_array.keys():
                if i in s :
                    print("Some values were not selected")
                    continue;
                else:
                    nppp_array = np_array.append(npp_array[i])
            try:
                path = "/Users/Sonu/pickle/ptrained_random_forest(test).pkl"
                path1 = "/Users/Sonu/pickle/ptrained_random_forest(classifier1).pkl"
                path2 = "/Users/Sonu/pickle/ptrained_random_forest(classifier2).pkl"
                path3 = "/Users/Sonu/pickle/ptrained_random_forest(classifier3).pkl"
                ranmdl = joblib.load(path)
                ranmdl1 = joblib.load(path1)
                ranmdl2 = joblib.load(path2)
                ranmdl3 = joblib.load(path3)
                print("successfully loaded")
                np_array = np.array(np_array)
                np_array = np_array.reshape(1,-1)
                pred = ranmdl.predict(np_array)
                pred = 10*pred

                avg = np.average(pred)
                app1= ranmdl1.predict(np_array)
                app2=ranmdl2.predict(np_array)
                app3=ranmdl3.predict(np_array)
                pred=np.append(pred,app1)
                pred=np.append(pred,app2)
                pred=np.append(pred,app3)
                pred = np.append(pred,avg*10)
                data=pred.tolist()
                merit =((data[11]/2 + data[9]*5 + data[8]*2.5)/7.8)*10
                data = np.append(data,merit)

                obj = Student.objects.get(Email=npp_array['Email'])
                obj.pred_avg_marks = data[11]
                obj.I_sem = data[0]
                obj.II_sem = data[1]
                obj.III_sem = data[2]
                obj.IV_sem = data[3]
                obj.V_sem = data[4]
                obj.VI_sem = data[5]
                obj.VII_sem = data[6]
                obj.VIII_sem = data[7]
                obj.pred_cocur = data[8]
                obj.pred_intern = data[9]
                obj.pred_pack = data[10]
                obj.save()

                print("prediction done")
                print(data)
                return render(request,'basicapp/result.html',{"form":data,"datas":npp_array})
            except ValueError as e:
                print("prediction failure{}",e)
    return render(request,'basicapp/formpage.html',{"form":form })



def dash(request):
    query = request.GET.get('q')
    if query:
        result = Student.objects.filter(Q(id__icontains = query)| Q(First_Name__icontains = query)| Q(Time__icontains = query)).annotate(max_mark=Max('pred_avg_marks')).order_by('-max_mark')
    else:
        result = Student.objects.all().annotate(max_mark=Max('pred_avg_marks')).order_by('-max_mark')
    genF = Student.objects.filter(Gender = 2 ).count()
    genM = Student.objects.filter(Gender = 1 ).count()
    a = Student.objects.filter(pred_avg_marks__gte=90).count()
    b = Student.objects.filter(pred_avg_marks__range=(80,90)).count()
    c = Student.objects.filter(pred_avg_marks__range=(70,80)).count()
    d = Student.objects.filter(pred_avg_marks__range=(60,70)).count()
    e = Student.objects.filter(pred_avg_marks__range=(50,60)).count()
    f = Student.objects.filter(pred_avg_marks__range=(41,50)).count()
    g = Student.objects.filter(pred_avg_marks__lte= 40).count()
    marks=[a,b,c,d,e,f,g]
    fi1 = Student.objects.filter(Annual_family_income = 1).count()
    fi2 = Student.objects.filter(Annual_family_income = 2).count()
    fi3 = Student.objects.filter(Annual_family_income = 3).count()
    fi4 = Student.objects.filter(Annual_family_income = 4).count()
    fi5 = Student.objects.filter(Annual_family_income = 5).count()
    income = [fi1,fi2,fi3,fi4,fi5]
    recentavg = Student.objects.aggregate(Avg('pred_avg_marks'))
    try:
        recentavg = recentavg['pred_avg_marks__avg']/10.5
    except Exception as e:
        recentavg = 5.5
    recentmerit = Student.objects.annotate(i_sum=(F('pred_avg_marks')/2 + F('pred_intern')*5+ F('pred_cocur')*2.5)/7.8).aggregate(Avg('i_sum'))
    today = datetime.now()
    recent = Student.objects.filter(Time = today)
    df = pd.DataFrame(list(sd.objects.all().values()))
    pf = df.groupby('joinyear')['CGPA'].mean()
    df['merit'] = (df['CGPA']*5+df['Internship']*5+df['What_level_of_participation']*2.5)/6.69
    meritavg = df.groupby('joinyear')['merit'].mean()
    return render(request,'basic_app/dashboard.html',{"averages":pf,"rank":result,"m":genM,"f":genF,"marks":marks,"income":income,"recent":recent,"recentavg":recentavg,"merit":meritavg,"recentmerit":recentmerit} )

def result(request,id):
    res_data = get_object_or_404(Student,pk=id)
    #res_data.pred_avg_marks res_data.pred_intern res_data.pred_cocur
    merit =(( res_data.pred_avg_marks/2 + res_data.pred_intern*5 + res_data.pred_cocur*2.5)/7.8)*10
    res_data=res_data.__dict__
    res_data['merit'] = merit
    return render(request,'basic_app/dash_result.html',{"res_data":res_data})

def del_stu_data(request,id):
    del_data = get_object_or_404(Student,pk=id)
    del_data.delete()
    return redirect('basicapp:dash')
