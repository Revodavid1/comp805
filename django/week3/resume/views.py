from django.shortcuts import render

# Create your views here.

def home(request):
   '''
   Renders resume app home page
   '''
   context = {}
   return render(request,'home.html',context)