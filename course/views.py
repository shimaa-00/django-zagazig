from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def handle_course_request(request):
    return HttpResponse("<p> Course Response </p>")