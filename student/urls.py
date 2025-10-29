from django.urls import path , include
from .views import handle_student_request , student_name, student_id , return_index_html
urlpatterns = [
    # 127.0.0.1:8000/student
    path('' , handle_student_request , name = 'students' ),
    path('index_html' , return_index_html  , name = 'studentindex'),
    path ("<int:id>" , student_id , name = 'student_id') , # variable sent to function 
    path ("<str:name>" , student_name  , name = 'student_name' ), # variable sent to function    
]
