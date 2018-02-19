from django.shortcuts import render
from .models import Education, Experience, Resume
# Create your views here.

def home(request):
    """
    renders the resume home template
    """ 
    address = "400 Commercial Street, Manchester, NH, 03101"
    phone = "(603) 289-0134"
    email = "odo1001@wildcats.unh.edu"
    skills = ["Django","Python"]
    context = {}
    first_resume = Resume.objects.first()
    experiences = Experience.objects.order_by('title')
    context = {'my_addr':address,'my_phone':phone,"my_email":email,
    'my_skills':skills,'my_res':first_resume}
    return render(request,'resume/home.html',context)
