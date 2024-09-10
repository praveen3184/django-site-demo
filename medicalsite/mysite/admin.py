from django.contrib import admin
from .models import Course,academicYear,Cateogry,courseDetails

# Register your models here
admin.site.register(Course)
admin.site.register(academicYear)
admin.site.register(Cateogry)
admin.site.register(courseDetails)