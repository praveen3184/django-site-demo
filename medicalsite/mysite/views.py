from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import courseDetails


# Create your views here.

def index(request):
    course_list = courseDetails.objects.order_by("academicYear")
    template = loader.get_template('index.html') 
    context = {'course_details': course_list}
    return HttpResponse(template.render(context, request))
    #return HttpResponse(request)

