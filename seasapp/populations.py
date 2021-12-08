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

    # Course_T
    file= filename.name
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COURSE_NAME','CREDIT_HOUR','SCHOOL_TITLE'],skiprows=3,nrows=1000)
    for courseID,courseName,creditHour,schoolT in zip(df.COFFER_COURSE_ID,df.COURSE_NAME,df.CREDIT_HOUR,
                            df.SCHOOL_TITLE): 
           
                course_model = Course_T(courseID=courseID,courseName=courseName,
                                    creditHour=creditHour,schoolTitle_id=schoolT)
                                    
                course_model.save()
                print(schoolT)

    # Room_T
    df = pd.read_excel(filename,usecols=['ROOM_ID',"ROOM_CAPACITY"],skiprows=3,nrows=1000)
    for roomID,roomCapacity in zip(df.ROOM_ID,df.ROOM_CAPACITY):
        
            room_model = Room_T(roomID=roomID,roomSize=roomCapacity)
            room_model.save()
    
    # Faculty_T
    df = pd.read_excel(filename,usecols=['FACULTY_FULL_NAME'],skiprows=3,nrows=1000) 

    for faculty in df.FACULTY_FULL_NAME:
       (id,name)= faculty.split('-')
       Faculty_model = Faculty_T(facultyID=id,facultyName=name)
       Faculty_model.save()

    # Section_T
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','SECTION','CAPACITY',
                    'ENROLLED','ROOM_ID','BLOCKED','FACULTY_FULL_NAME','STRAT_TIME',
                    'END_TIME','ST_MW'],skiprows=3,nrows=1000) 
    (a,b,c,semester,year)=filename.name.split(' ')
    (y,f)=year.split('.')
    for courseID,section,capacity,enrolled,roomid,blocked,faculty,start,end,day in zip(df.COFFER_COURSE_ID,df.SECTION,df.CAPACITY,
                    df.ENROLLED,df.ROOM_ID,df.BLOCKED,df.FACULTY_FULL_NAME,df.STRAT_TIME,
                    df.END_TIME,df.ST_MW):
        (id,name)= faculty.split('-')
        section_model=Section_T(sectionNo=section,courseID_id=courseID,capacity=capacity,
                 enrolled=enrolled,roomID_id=roomid,blocked=blocked,facultyID_id=id,startTime=start,endTime=end,
                 day=day,semester=semester,year=y)

        section_model.save()

    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COFFERED_WITH'],skiprows=3,nrows=1000)
    for courseID,offeredWith in zip(df.COFFER_COURSE_ID,df.COFFERED_WITH): 
           
            course_model = Course_T(offeredCourseID_id=courseID,coofferredwith_id=offeredWith)                  
            course_model.save()



