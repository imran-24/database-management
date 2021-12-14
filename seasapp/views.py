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
        
def resource_usage(request):
    if request.method =='GET':
            print('true')
            semester = request.GET.get('Semester')
            year = request.GET.get('Year')
            print(semester)
            print(year)
            
            usage = IUB_resource(semester,year)
            s = (usage['sections'][0]+usage['sections'][1] + usage['sections'][2]+usage['sections'][3]+usage['sections'][4])
            e = (usage['enrolled'][0]+usage['enrolled'][1] + usage['enrolled'][2] + usage['enrolled'][3] + usage['enrolled'][4])/5
            r = (usage['roomcap'][0]+usage['roomcap'][1]+usage['roomcap'][2]+usage['roomcap'][3]+usage['roomcap'][4])/5
            d = (usage['waste'][0]+usage['waste'][0]+usage['waste'][0]+usage['waste'][0]+usage['waste'][0])/5
            p = (usage['percent'][4]+usage['percent'][4]+usage['percent'][4]+usage['percent'][4]+usage['percent'][4])/5
           
            a1=[s,e,r,d,str(p)+'%']

            a2=[usage['sections'][0],usage['enrolled'][0],usage['roomcap'][0],usage['waste'][0],str(usage['percent'][0])+'%']
            a3=[usage['sections'][1],usage['enrolled'][1],usage['roomcap'][1],usage['waste'][1],str(usage['percent'][1])+'%']
            a4=[usage['sections'][2],usage['enrolled'][2],usage['roomcap'][2],usage['waste'][2],str(usage['percent'][2])+'%']
            a5=[usage['sections'][3],usage['enrolled'][3],usage['roomcap'][3],usage['waste'][3],str(usage['percent'][3])+'%']
            a6=[usage['sections'][4],usage['enrolled'][4],usage['roomcap'][4],usage['waste'][4],str(usage['percent'][4])+'%']
            a8=[r,e,d,p]
            context={
                'a1':a1,
                'a2':a2,
                'a3':a3,
                'a4':a4,
                'a5':a5,
                'a6':a6,
                'a7':semester,
                'a8': r,
                'a9': e,
                'a10':d,
                'a11':p
            }
            return render(request,'resource_usage.html',context=context)
def classroom(request):
    return render(request,'classroom.html',{})

