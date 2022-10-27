from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm
import json
from django.core import serializers


def getAllStudents(request):
    allStudents = serializers.serialize('json', Student.objects.all())
    return JsonResponse(json.loads(allStudents), safe=False)


def createStudent(request):
    newStudent = StudentForm(request.POST)
    if newStudent.is_valid():
        newStudent.save()
        return JsonResponse(newStudent.data, status=201)
    else:
        return JsonResponse(newStudent.errors, status=409)


def studentsController(request):
    if request.method == 'GET':
        return getAllStudents(request)
    if request.method == 'POST':
        return createStudent(request)


def getOneStudent(request, id):
    data = serializers.serialize('json', Student.objects.all().filter(id=id))
    return JsonResponse(json.loads(data), safe=False)


def updateOneStudent(request, id):
    obj = get_object_or_404(Student, id=id)
    student = StudentForm(request.POST, instance=obj)
    if student.is_valid():
        student.save()
        return JsonResponse(student.data)
    else:
        return JsonResponse(student.errors, status=400)


def deleteOneStudent(request, id):
    obj = get_object_or_404(Student, id=id)
    obj.delete()
    return JsonResponse({'status': 'success'})


def oneStudentController(request, id):
    if request.method == 'GET':
        return getOneStudent(request, id)
    elif request.method == 'POST':
        return updateOneStudent(request, id)
    elif request.method == 'DELETE':
        return deleteOneStudent(request, id)
    else:
        return JsonResponse({'message:': 'method not allowed'}, status=405)
