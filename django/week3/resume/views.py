from django.shortcuts import render
from .models import Education, Experience
# Create your views here.

def home(request):
	"""
	renders the resume home template
	"""	
	educations = Education.objects.all()
	experiences = Experience.objects.all()
	context = {'my_education':educations,'my_experiences':experiences}
	return render(request,'resume/home.html',context)
