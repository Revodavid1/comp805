from django.shortcuts import render
from .models import Education, Experience
# Create your views here.

def home(request):
	"""
	renders the resume home template
	"""	
	name = "Omu Oreva"
	address = "400 Commercial Street, Manchester, NH, 03101"
	phone = "(603) 289-0134"
	email = "odo1001@wildcats.unh.edu"
	skills = ["Django","Python"]
	context = {}
	educations = Education.objects.order_by('degree')
	experiences = Experience.objects.order_by('title')
	context = {'my_education':educations,'my_experiences':experiences,
	'my_name':name,'my_addr':address,'my_phone':phone,"my_email":email,
	"my_skills":skills}
	return render(request,'resume/home.html',context)
