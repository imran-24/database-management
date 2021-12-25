from io import DEFAULT_BUFFER_SIZE
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

    
    # Department_T
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
    # Course_T
    file= filename.name
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COURSE_NAME','CREDIT_HOUR','SCHOOL_TITLE',"Dept"])
    for courseID,courseName,creditHour,schoolTitle,dept in zip(df.COFFER_COURSE_ID,df.COURSE_NAME,df.CREDIT_HOUR,
                            df.SCHOOL_TITLE,df.Dept): 
            
            schoolTitle = School_T.objects.filter(schoolTitle=schoolTitle).first()
            dept =Department_T.objects.filter(departmentName=dept).first()
            try:
                course_model = Course_T(courseID=courseID,courseName=courseName,
                                        creditHour=creditHour,schoolTitle=schoolTitle,departmentName=dept)
                                            
                course_model.save()
            except Exception as E:
                pass
            

    # Room_T
    df = pd.read_excel(filename,usecols=['ROOM_ID',"ROOM_CAPACITY"])
    for roomID,roomCapacity in zip(df.ROOM_ID,df.ROOM_CAPACITY):
        
            room_model = Room_T(roomID=roomID,roomSize=roomCapacity)
            room_model.save()
    
    # Faculty_T
    df = pd.read_excel(filename,usecols=['FACULTY_FULL_NAME']) 
    i = 2
    for faculty in df.FACULTY_FULL_NAME:
        # try:
        
        (id,name)= faculty.split('-',1)
        if 'TBA' not in name:
            Faculty_model = Faculty_T(facultyID=id,facultyName=name)
            Faculty_model.save()
           

    # Section_T
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','SECTION','ENROLLED','ROOM_ID','BLOCKED','FACULTY_FULL_NAME','STRAT_TIME','END_TIME','ST_MW','CAPACITY','Semester','Year']) 
    
    df['CAPACITY'].fillna(0,inplace= True)
    
    i = 2
    for courseID,section,enrolled,roomid,blocked,faculty,start,end,day,capacity,semester,y in zip(df.COFFER_COURSE_ID,df.SECTION,df.ENROLLED,df.ROOM_ID,df.BLOCKED,df.FACULTY_FULL_NAME,df.STRAT_TIME,df.END_TIME,df.ST_MW,df.CAPACITY,df.Semester,df.Year):
                courseID = Course_T.objects.filter(courseID= courseID).first()
                
                i += 1
                (id,name)= faculty.split('-',1)
                facultyID = Faculty_T.objects.filter(facultyID=id).first()
                roomid = Room_T.objects.filter(roomID= roomid).first()
                try:
                    section_model=Section_T(sectionNo=section,courseID=courseID,enrolled = enrolled,roomID = roomid,blocked = blocked,facultyID= facultyID,startTime = start,endTime = end ,day= day,capacity = capacity,semester=semester,year=y)
                    section_model.save()
                except Exception as e :
                    pass
           



    # OfferedCourse_T
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COFFERED_WITH'])
    for courseID,offeredWith in zip(df.COFFER_COURSE_ID,df.COFFERED_WITH): 
       
            courseID = Course_T.objects.filter(courseID=courseID).first()
           
            try:
                offeredWith = Course_T.objects.filter(courseID=offeredWith).first()
                course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith) 
                    
                course_model.save()
            except Exception as e:
                pass    
            
            try:
                (course1,course2)= offeredWith.split(',')

                offeredWith1 = Course_T.objects.filter(courseID=course1).first()
                offeredWith2 = Course_T.objects.filter(courseID=course2).first()
                if offeredWith1 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith1) 
                    
                if offeredWith2 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith2) 
                    
                course_model.save()
              
            except Exception as e1:
                pass

            try:
                (course1,course2,course3)= offeredWith.split(',')

                offeredWith1 = Course_T.objects.filter(courseID=course1).first()
                offeredWith2 = Course_T.objects.filter(courseID=course2).first()
                offeredWith3 = Course_T.objects.filter(courseID=course3).first()
                if offeredWith1 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith1) 
                    
                if offeredWith2 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith2) 

                if offeredWith3 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith3) 
                        
                course_model.save()
              
            except Exception as e1:
                pass
            
            
            try:
                (course1,course2,course3,course4)= offeredWith.split(',')

                offeredWith1 = Course_T.objects.filter(courseID=course1).first()
                offeredWith2 = Course_T.objects.filter(courseID=course2).first()
                offeredWith3 = Course_T.objects.filter(courseID=course3).first()
                offeredWith4 = Course_T.objects.filter(courseID=course3).first()
                if offeredWith1 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith1) 
                    
                if offeredWith2 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith2) 

                if offeredWith3 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith3) 

                if offeredWith4 is not None:
                    course_model = OfferedCourse_T(courseID=courseID,offeredWith=offeredWith4) 
                        
                course_model.save()
              
            except Exception as e1:
                pass
            
