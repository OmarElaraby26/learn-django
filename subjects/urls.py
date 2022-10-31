
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from subjects import views

from . import views
urlpatterns = [
    path('', views.SubjectList.as_view()),
    path('<int:id>', views.SubjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
