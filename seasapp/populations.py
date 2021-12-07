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
    
    SchoolT =["SBE","SETS","SELS","SLASS","SPPH"]
    for schoolTitle in SchoolT:
        try:
           school_model = School_T(schoolTitle=schoolTitle)
           school_model.save()
        except Exception as e:
            pass
    file= filename.name
    df = pd.read_excel(filename,usecols=['COFFER_COURSE_ID','COURSE_NAME','CREDIT_HOUR','SCHOOL_TITLE'],skiprows=3,nrows=26)
    for courseID,courseName,creditHour,schoolT in zip(df.COFFER_COURSE_ID,df.COURSE_NAME,df.CREDIT_HOUR,
                            df.SCHOOL_TITLE): 
           
                course_model = Course_T(courseID=courseID,courseName=courseName,
                                    creditHour=creditHour,schoolTitle=schoolT)
                course_model.save()
          

                print(schoolT)
