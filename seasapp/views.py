from decimal import Context
import json
from django.shortcuts import render
from .raw_sql import *
from json import dumps
# Create your views here.
# from seasapp.ra import classroom_requirement_course_offer
def success(request):
    return render(request,'success.html',{})

def classroom_requirement(request):
        if request.method =='GET':
            print('true')
            semester = request.GET.get('Semester')
            year = request.GET.get('Year')
            print(semester)
            print(year)
            section = classroom_requirement_course_offer(semester,year)
            print(section)
        class6=[]
        for cls in section:
            cls = int(cls/12)
            class6.append(cls) 
        print(class6)
        
        class7=[]
        for cls in section:
            cls = int(cls/14)
            class7.append(cls) 
        print(class7)
        a1 = [ section[0], class6[0], class7[0]]
        a2 = [ section[1], class6[1], class7[1]]
        a3 = [ section[2], class6[2], class7[2]]
        a4 = [ section[3], class6[3], class7[3]]
        a5 = [ section[4], class6[4], class7[4]]
        a6 = [ section[5], class6[5], class7[5]]
        a7 = [ section[6], class6[6], class7[6]]
        a8 = [ section[7], class6[7], class7[7]]

        context= {
            'a1' : a1,
            'a2' : a2,
            'a3' : a3,
            'a4' : a4,
            'a5' : a5,
            'a6' : a6,
            'a7' : a7,
            'a8' : a8,
            'year': year,
            'semester':semester
           }  
        context['class6'] = json.dumps(class6)
        context['class7'] = json.dumps(class7)
        
        
        # print(type(context))
        # print(context)
       
       
        return render(request,'classroom_view.html',context)
        # print("Not a post method")
        # return render(request,'classroom_view.html',{})
        

def classroom(request):
    return render(request,'classroom.html',{})

