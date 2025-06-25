from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Student 
from .forms import StudentForm
# Create your views here.
def homePage(request, id):
    xyz = Student.objects.all()
    context = {
        "data" : xyz,
      
    }
    # try:
    #     ls = context['ls'][id]
    # except Exception as e :
    #     return HttpResponse("page not found")  
   
   
    return render(request, 'myapp/index.html', context)

def aboutUs(request):
    return HttpResponse("Hello, My name is Sherya")

def student_form(request):
    if request.method == 'GET':
        form = StudentForm(request. POST)    
        if form.is_valid():
            form.save()  # save to DB
            return render(request, 'myapp/success.html')  # or redirect
    else:
        form = StudentForm()
    
    return render(request, 'myapp/student_form.html', {'form': form})


