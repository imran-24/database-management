from django.db import models

# Create your models here.
class ModelWithFileField(models.Model):
    file_field = models.FileField() 
    
class School_T(models.Model):
    schoolTitle = models.CharField(max_length=5, primary_key=True)
    

    def __str__(self):
        return self.schoolTitle

class Department_T(models.Model):
    # DeptID = models.CharField(max_length=6, primary_key=True)
    departmentName = models.CharField(max_length=50,primary_key=True)
    schoolTitle = models.ForeignKey(School_T,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self. departmentName

class Course_T(models.Model):
    offeredCourseID = models.CharField(max_length=7, primary_key=True)
    courseName = models.CharField(max_length=100)
    creditHour = models.IntegerField()
    departmentName= models.ForeignKey(Department_T, null=True, on_delete=models.CASCADE)
    schoolTitle = models.ForeignKey(School_T,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.offeredCourseID

class CoOfferedCourse_T(models.Model):
    offeredCourseID = models.ForeignKey(Course_T, on_delete=models.CASCADE,null=True)
    coofferredwith = models.CharField(max_length=50,default=offeredCourseID)

    class Meta:
        unique_together = (("offeredCourseID", "coofferredwith"),)


class Room_T(models.Model):
    roomID = models.CharField(max_length=9, primary_key=True)
    roomSize = models.IntegerField()

    def __str__(self):
        return self.roomID

class Faculty_T(models.Model):
    facultyID = models.CharField(max_length =5,primary_key=True)
    facultyName = models.CharField(max_length=50)
    departmentName = models.ForeignKey(Department_T, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.facultyID)

class Section_T(models.Model):
    # sectionID = models.CharField(max_length=40, primary_key=True)
    sectionNo = models.IntegerField()
    offeredCourseID = models.ForeignKey(Course_T,null=True,on_delete=models.CASCADE)
    capacity = models.IntegerField(null=True)
    enrolled = models.IntegerField(null=True)
    blocked = models.CharField(max_length=3, null=True) 
    roomID = models.ForeignKey(Room_T, null=True, on_delete=models.CASCADE)
    facultyID = models.ForeignKey(Faculty_T, null=True, on_delete=models.CASCADE)
    startTime = models.CharField(max_length=10,null=True)
    endTime = models.CharField(max_length=10,null = True)
    day = models.CharField(max_length=10, null=True)
    semester = models.CharField(max_length=6)
    year = models.IntegerField()
   

    class Meta:
        unique_together = (("offeredCourseID","sectionNo","semester", "year"),)

    def __str__(self):
        return str(self.sectionNo)