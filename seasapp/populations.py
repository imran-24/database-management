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

    file= filename.name
    df = pd.read_excel(filename,usecols=['SCHOOL_TITLE'],skiprows=3,nrows=4)
    for schoolTitle in df.SCHOOL_TITLE:
        school_model = School_T(schoolTitle=schoolTitle)
        school_model.save()
        print(schoolTitle)
