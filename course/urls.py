from django.urls import path
from .views import handle_course_request
urlpatterns = [
     # 127.0.0.1:8000/course/
    path("" ,handle_course_request )
]
