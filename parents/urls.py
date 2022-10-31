
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from parents import views

from . import views
urlpatterns = [
    path('', views.ParentList.as_view()),
    path('<int:id>', views.ParentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
