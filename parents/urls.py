
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.parentsController),
    path('<int:id>', views.oneParentController),
]
