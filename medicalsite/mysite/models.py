from django.db import models

# Create your models here.

class Course(models.Model):
    course_text = models.CharField(max_length=255)

    def __str__(self):
        return self.course_text

class academicYear(models.Model):
    years_text = models.CharField(max_length=255)

    def __str__(self):
        return self.years_text
    
class Cateogry(models.Model):
    category_text = models.CharField(max_length=255)

    def __str__(self):
        return self.category_text
    
class courseDetails(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    academicYear = models.ForeignKey(academicYear, on_delete=models.CASCADE)
    cateogry = models.ForeignKey(Cateogry, on_delete=models.CASCADE)
    filePath = models.FileField(upload_to="pdfFilePath")

    def __str__(self):
        return f'{self.course}{self.academicYear}{self.cateogry}{self.filePath}'  
       # return (self.course,self.academicYear,self.cateogry,self.filePath)