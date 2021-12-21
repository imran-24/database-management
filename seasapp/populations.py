from os import execlp
from django.db.models.fields import NullBooleanField
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UploadFileForm
from .models import *
import pandas as pd


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            instance = ModelWithFileField(file_field=file)
            instance.save()
            populate(file)
            return redirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



def populate(filename):
    # SchoolT
    SchoolT =["SBE","SETS","SELS","SLASS","SPPH"]
    for schoolTitle in SchoolT:
        try:
           school_model = School_T(schoolTitle=schoolTitle)
           school_model.save()
        except Exception as e:
            pass

    # # Course_T
    # file= filename.name
    # df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COURSE_NAME','CREDIT_HOUR','SCHOOL_TITLE'])
    # for courseID,courseName,creditHour,schoolTitle in zip(df.COFFER_COURSE_ID,df.COURSE_NAME,df.CREDIT_HOUR,
    #                         df.SCHOOL_TITLE): 
            
    #         schoolTitle = School_T.objects.filter(schoolTitle=schoolTitle).first()
    #         print(schoolTitle)
    #         course_model = Course_T(offeredCourseID=courseID,courseName=courseName,
    #                                 creditHour=creditHour,schoolTitle=schoolTitle)
                                         
    #         course_model.save()
    #         # except Exception as e:
    #         #     pass
               

    # # Room_T
    # df = pd.read_excel(filename,usecols=['ROOM_ID',"ROOM_CAPACITY"])
    # for roomID,roomCapacity in zip(df.ROOM_ID,df.ROOM_CAPACITY):
        
    #         room_model = Room_T(roomID=roomID,roomSize=roomCapacity)
    #         room_model.save()
    
    # # Faculty_T
    # df = pd.read_excel(filename,usecols=['FACULTY_FULL_NAME']) 
    # i = 2
    # for faculty in df.FACULTY_FULL_NAME:
    #     # try:
        
    #     (id,name)= faculty.split('-',1)
    #     if 'TBA' not in name:
    #         Faculty_model = Faculty_T(facultyID=id,facultyName=name)
    #         Faculty_model.save()
    #         print(id)
    #         print(name)
        
    #     print(i)
    #     i += 1
    #     # except Exception as e:
    #     #     pass

    # Section_T
    # df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','SECTION','ENROLLED','ROOM_ID','BLOCKED','FACULTY_FULL_NAME','STRAT_TIME','END_TIME','ST_MW','CAPACITY','Semester','Year']) 
    
    # df['CAPACITY'].fillna(0,inplace= True)
    
    # i = 2
    # for courseID,section,enrolled,roomid,blocked,faculty,start,end,day,capacity,semester,y in zip(df.COFFER_COURSE_ID,df.SECTION,df.ENROLLED,df.ROOM_ID,df.BLOCKED,df.FACULTY_FULL_NAME,df.STRAT_TIME,df.END_TIME,df.ST_MW,df.CAPACITY,df.Semester,df.Year):
    #             courseID = Course_T.objects.filter(offeredCourseID= courseID).first()
    #             print(courseID)
    #             print(i)
                
    #             i += 1
    #             (id,name)= faculty.split('-',1)
    #             facultyID = Faculty_T.objects.filter(facultyID=id).first()
    #             roomid = Room_T.objects.filter(roomID= roomid).first()
    #             section_model=Section_T(sectionNo=section,offeredCourseID=courseID,enrolled = enrolled,roomID = roomid,blocked = blocked,facultyID= facultyID,startTime = start,endTime = end ,day= day,capacity = capacity,semester=semester,year=y)
    #             section_model.save()
            
           
              

        
    Department_T
    df = pd.read_excel(filename,usecols=['Dept','SCHOOL_TITLE'])
    school=["SBE","SETS","SELS","SLASS","SPPH"]
    for dept,schoolTitle in  zip(df.Dept,df.SCHOOL_TITLE):
        try:
            if dept  in school:
                continue
            else:
                schoolTitle = School_T.objects.filter(schoolTitle=schoolTitle).first()
                Department_model = Department_T(departmentName=dept,schoolTitle=schoolTitle)
                Department_model.save()
        except Exception as e:
            pass  


    CoOfferedCourse_T
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COFFERED_WITH'])
    for courseID,offeredWith in zip(df.COFFER_COURSE_ID,df.COFFERED_WITH): 
       
            courseID = Course_T.objects.filter(offeredCourseID=courseID).first()
            try:
                (course1,course2)= offeredWith.split(',')
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course1) 
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course2)                  
                
                course_model.save() 
            except Exception as e1:
                pass

            try:
                (course1,course2,course3)= offeredWith.split(',')
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course1) 
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course2)     
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course3)                              
                
                course_model.save() 
            except Exception as e2:
                pass
            
            try:
                (course1,course2,course3,course4)= offeredWith.split(',')
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course1) 
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course2)     
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course3)                              
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course4)                              

                course_model.save() 
            except Exception as e1:
                pass

            try:
                (course1,course2,course3,course4,course5)= offeredWith.split(',')
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course1) 
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course2)     
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course3)                              
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course4)                              
                course_model = CoOfferedCourse_T(offeredCourseID=courseID,coofferredwith=course5)                              

                course_model.save() 
            except Exception as e1:
                pass

       
       


