from django.shortcuts import render

def home(request):
	'''
	Renders home page
	'''
	context = {}
	return render(request,'home.html',context)

def resume(request):
	'''
	Renders resume page
	'''
	name = "Omu Oreva"
	address = "400 Commercial Street, Manchester, NH, 03101"
	phone = "(603) 289-0134"
	email = "odo1001@wildcats.unh.edu"
	skills = ["Django","Python"]
	context = {'my_name':name,'my_addr':address,'my_phone':phone,"my_email":
	email,"my_skills":skills}
	return render(request,'resume.html',context)

def portfolio(request):
	'''
	Renders portfolio page
	'''
	context = {}
	return render(request,'portfolio.html',context)
