from decimal import Context
import json
from django.shortcuts import render

from seasapp.models import School_T
from .raw_sql import *
from json import dumps

# Create your views here.
# from seasapp.ra import classroom_requirement_course_offer
def success(request):
    return render(request,'success.html',{})

def home(request):
    return render(request,'seas/home.html',{})

def classroom_requirement(request):
        if request.method =='POST':
            print('true')
            semester = request.POST.get('Semester')
            year = request.POST.get('Year')
            print(semester)
            print(year)
            section = classroom_requirement_course_offer(semester,year)
            print(section)
        class6=[]
        for cls in section:
            cls = int(cls/12)
            class6.append(cls) 
        print(class6)
        print(type(class6))
        class7=[]
        for cls in section:
            cls = int(cls/14)
            class7.append(cls) 
        print(class7)
        print(type(class7))
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
       
       
        return render(request,'classroom_view.html',context=context)


def usage_of_resource(request):
    if request.method =='POST':
            print('true')
            semester = request.POST.get('Semester')
            year = request.POST.get('Year')
            print(semester)
            print(year)
            
            usage = IUB_resource_usage(semester,year)
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
            return render(request,'resource_usage_view.html',context=context)

def available_resource(request):
   
    if request.method == "GET":
        s = IUB_Available_resource( )
        

        a1=[s['room'][0],s['space'][0],s['room'][0]*s['space'][0]]
        a2=[s['room'][1],s['space'][1],s['room'][1]*s['space'][1]]
        a3=[s['room'][2],s['space'][2],s['room'][2]*s['space'][2]]
        a4=[s['room'][3],s['space'][3],s['room'][3]*s['space'][3]]
        a5=[s['room'][4],s['space'][4],s['room'][4]*s['space'][4]]
        a6=[s['room'][5],s['space'][5],s['room'][4]*s['space'][4]]
        # a7=[s['room'][6],s['space'][6],s['room'][6]*s['space'][6]]
        # a8=[s['room'][7],s['space'][7],s['room'][7]*s['space'][7]]
        # a9=[s['room'][8],s['space'][8],s['room'][8]*s['space'][8]]
        # a10=[s['room'][9],s['space'][9],s['room'][9]*s['space'][9]]
        
        
        context={
            'a1':a1,
            'a2':a2,
            'a3':a3,
            'a4':a4,
            'a5':a5,
            'a6':a6,
            # 'a7':a7,
            # 'a8':a8,
            # 'a9':a9,
            # 'a10':a10
        }
        
    return render(request,'available_resource.html',context)

def Availability_course_offering_comparison(request):
    if request.method =='POST':
            semester = request.POST.get('Semester')
            year = request.POST.get('Year')
            print(semester)
            print(year)
            section = classroom_requirement_course_offer(semester,year)
            print(section)
            class6=[]
            for cls in section:
                cls = int(cls/12)
                class6.append(cls) 
            print('class6')
            print(class6)
            cl = 0 
            for cls in range(len(class6)):
                cl += class6[cls]
                 
            s = IUB_Available_resource()
            S = 0
            resource=[]
            for r in s['space']:
                resource.append(r)
                S += r

            b1=s['space'][0]-(class6[0]+class6[1])
            b2=s['space'][1]-class6[2]
            b3=s['space'][2]-class6[3]
            b4=s['space'][3]-class6[4]
            b5=s['space'][4]-class6[5]
            b6=s['space'][5]-class6[6]
            c1=b1 + b2 + b3 + b4  + b5 + b6 
            dif=[b1,b2,b3,b4,b5,b6]
            sec=[class6[0]+class6[1],class6[2],class6[3],class6[4],class6[5],class6[6]]
            a1=[s['room'][0],s['space'][0],class6[0]+class6[1],b1]
            a2=[s['room'][1],s['space'][1],class6[2],b2]
            a3=[s['room'][2],s['space'][2],class6[3],b3]
            a4=[s['room'][3],s['space'][3],class6[4],b4]
            a5=[s['room'][4],s['space'][4],class6[5],b5]
            a6=[s['room'][5],s['space'][5],class6[6],b6]
            a8=[S,cl,c1]
            # a7=[s['room'][6],s['space'][6],s['room'][6]*s['space'][6],s['space']-class6[7]]
            # a8=[s['room'][7],s['space'][7],s['room'][7]*s['space'][7],s['space']-class6[8]]
            # a9=[s['room'][8],s['space'][8],s['room'][8]*s['space'][8],s['space']-class6[9]]
            # a10=[s['room'][9],s['space'][9],s['room'][9]*s['space'][9],s['space']-class6[10]]

            context={
            'a1':a1,
            'a2':a2,
            'a3':a3,
            'a4':a4,
            'a5':a5,
            'a6':a6,
            'a7':semester,
            'a8':a8,
            # 'a9':a9,
            # 'a10':a10
            }
            context['resource']=json.dumps(resource)
            print(context['resource'])
            context['sec']=json.dumps(sec)
            print(context['sec'])
            context['dif']=json.dumps(dif)
            print(context['dif'])

    return render(request,'AvailabilityVScourse_offering_view.html',context=context)

# def section_based_on_enrollment(request):
#     if request.method == 'GET':
#         semester = request.GET.get('Semester')
#         year = request.GET.get('Year')
#         SBE = sections_based_on_enrolled(semester,year,'SBE')
#         SELS = sections_based_on_enrolled(semester,year,'SELS')
#         SETS = sections_based_on_enrolled(semester,year,'SETS')
#         SLASS = sections_based_on_enrolled(semester,year,'SLASS')
#         SPPH = sections_based_on_enrolled(semester,year,'SPPH')
        
#         # sec =[]
#         # for a in range(62):
#         #     SBE1 =[]
#         #     s = 0
#         #     s = a
#         #     b = s+1
#         #     print(s)
#         #     while SBE[a][a] != b:
#         #         SBE1.append("")
#         #         b += 1
#         #     SBE1.append(SBE[a][s+1])

#             #  
#             # if SELS[s][s] == s+1:
#             #     list.append(SELS[s][s+1])
#             # # if SETS[s][s] == s+1:
#             # #     list.append(SETS[s][s+1])
#             # if SLASS[s][s] == s+1:
#             #     list.append(SLASS[s][s+1])
#             # if SPPH[s][s] == s+1:
#             #     list.append(SPPH[s][s+1])

#             sec.append(list)
#         context={
#             'section':sec,
#         }

#     return render(request,'section_based_on_enrollment/html',context=context)

def Enrollment_wise_course_distribution(request):
    if request.method == "POST":
        print(True)
        semester = request.POST.get('Semester')
        print(semester)
        year = request.POST.get('Year')
        print(year)
        sbe=enrollment_wise_course_distribution(semester,year,'SBE')
        sels=enrollment_wise_course_distribution(semester,year,'SELS')
        sets=enrollment_wise_course_distribution(semester,year,'SETS')
        slass=enrollment_wise_course_distribution(semester,year,'SLASS')
        spph=enrollment_wise_course_distribution(semester,year,'SPPH')
        print("SBE")
        print(sbe)
        # sbe.insert(0,'SBE')
        # sels.insert(0,'SELS')
        # sets.insert(0,'SETS')
        # slass.insert(0,'SLASS')
        # spph.insert(0,'SPPH')
        # sbe.insert(0,'41-50')
        # sbe.insert(0,'51-55')
        # sbe.insert(0,'56-60')
        # sbe.insert(0,'1-10')
        print('SELS')
        print(sels)
        print('SETS')
        print(sets)
        print('SLASS')
        print(slass)
        print('SPPH')
        print(spph)
        # title= ['Enrollment','SBE','SELS','SETS','SLASS','SPPH','Total']
        name = ['1-10','11-20','21-30','31-35','36-40','41-50','51-55','56-60','60+']
        row = []
        total=[]
        for n in range(9):
            Total = 0
            a= sbe[n]
            b= sels[n]
            c= sets[n]
            d= slass[n]
            e= spph[n]
            # print(a)
            # print(b)
            # print(c)
            # print(d)
            # print(e)
            Total = a+b+c+d+e
            total.append(Total)
            row.append([name[n],a,b,c,d,e,Total])
        context = {
            'row':row,
            'semester':semester,
            'name': name
        }
        context['sbe_'] = json.dumps(sbe)
        print('-----')
        
        context['sels_'] = json.dumps(sels)
        context['sets_'] = json.dumps(sets)
        context['slass_'] = json.dumps(slass)
        context['spph_'] = json.dumps(spph)
        
    return render(request,'course_distribution_view.html',context= context)

def revenue_of_IUB(request):
    if request.method == "POST":
        print(True)
        FromYear = request.POST.get('YearF')
        print(FromYear)
        ToYear = request.POST.get('YearT')
        print(ToYear)
        
        School=[]
        rows=[]
        
        semester=["Spring",'Summer','Autumn']
        school = School_T.objects.all()
        while int(FromYear) <= int(ToYear) :
            sum = 0
            i = 0
            for i in range(len(semester)):
                j = 0
                scl = str(FromYear)+str(i)+semester[i]
                School.append(scl)
                for j in range(len(school)):
                    num = School.append(enrollment_wise_course_distribution(semester[i],FromYear,school[j]))
                    if num is None:
                        pass 
                    else: 
                        sum += num
                School.append(sum)
                rows.append(School)
                print(rows)
                FromYear = int(FromYear) + 1

                context={
                    'revenue': rows
                }
        return render(request,'revenue_view.html',context= context)

def classroom(request):
    return render(request,'classroom.html',{})

def course_distribution(request):
    return render(request,'course_distribution.html',{})

def resource_usage(request):
    return render(request,'resource_usage.html',{})

def Availability_course_offering(request):
    return render(request,'AvailabilityVScourse_offering.html',{})


def IUB_revenues(request):
    return render(request,'revenue.html',{})
