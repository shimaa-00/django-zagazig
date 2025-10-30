from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def handle_student_request(request):
    response = HttpResponse("<h1> http response </h1>")
    return response
def student_name(request , name):
    return HttpResponse(f"studnet name :  {name}")
def student_id (request , id ):
    return HttpResponse(f"studnet id :  {id}")

def return_index_html ( request):
    studnets = [{"name" : "mohammed" , "age" : 23 , "gpa" :2.5} , {} , {}]
    context = {"name" : "amer" , "age": 23 , 'courses' : ["python" , "html" , "css"]}
    return render (request  , 'student/index.html'  , context=context )
from .models import Student

def returns_students_from_db(request):
    # select * from student_student ;
    students = Student.objects.all() 
    return render (request , 'student/list.html' , {"students" :students})