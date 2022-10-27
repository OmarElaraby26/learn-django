
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.studentsController),
    path('<int:id>', views.oneStudentController),
]
