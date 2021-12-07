from django.shortcuts import render

# Create your views here.
def success(request):
    return render(request,'success.html',{})
