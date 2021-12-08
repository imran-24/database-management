from django.contrib import admin
from .models import *
# Register your models here.

class School_TAdmin(admin.ModelAdmin):
    list_display =['schoolTitle',]
    search_fields= ['schoolTitle',]

admin.site.register(School_T, School_TAdmin)


class Department_TAdmin(admin.ModelAdmin):
    list_display = ['departmentName','schoolTitle',]
    search_fields= ['departmentName','schoolTitle',]

admin.site.register(Department_T, Department_TAdmin)


class Faculty_TAdmin(admin.ModelAdmin):
    list_display = ['facultyID','facultyName','departmentName',]
    search_fields=['facultyID','facultyName','departmentName',]

admin.site.register(Faculty_T, Faculty_TAdmin)


class Course_TAdmin(admin.ModelAdmin):
    list_display = ['courseID','courseName','creditHour','departmentName',]
    search_fields=['courseID','courseName','creditHour','departmentName',]
admin.site.register(Course_T, Course_TAdmin)


class CourseOfferedWith_TAdmin(admin.ModelAdmin):
    list_dislay =['offeredCourseID','coofferredwith',]
    search_fields=['offeredCourseID','coofferredwith']

admin.site.register(CoOfferedCourse_T,CourseOfferedWith_TAdmin)

class Room_TAdmin(admin.ModelAdmin):
    list_display = ['roomID','roomSize']
    search_fields= ['roomID','roomSize']

admin.site.register(Room_T, Room_TAdmin)



class Section_TAdmin(admin.ModelAdmin):
    list_display = ['sectionNo','courseID','capacity','enrolled','blocked',
    'roomID','facultyID','startTime','endTime','day','semester','year']
    search_fields=['sectionNo','courseID','capacity','enrolled','blocked',
    'roomID','facultyID','startTime','endTime','day','semester','year']

admin.site.register(Section_T, Section_TAdmin)