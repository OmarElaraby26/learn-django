
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from students import views

from . import views
urlpatterns = [
    path('', views.StudentList.as_view()),
    path('<int:id>', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
