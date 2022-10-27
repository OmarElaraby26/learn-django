from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Subject
from .forms import SubjectForm
import json
from django.core import serializers


def getAllSubjects(request):
    allSubjects = serializers.serialize('json', Subject.objects.all())
    return JsonResponse(json.loads(allSubjects), safe=False)


def createSubject(request):
    newSubject = SubjectForm(request.POST)
    if newSubject.is_valid():
        newSubject.save()
        return JsonResponse(newSubject.data, status=201)
    else:
        return JsonResponse(newSubject.errors, status=409)


def subjectsController(request):
    if request.method == 'GET':
        return getAllSubjects(request)
    if request.method == 'POST':
        return createSubject(request)


def getOneSubject(request, id):
    data = serializers.serialize('json', Subject.objects.all().filter(id=id))
    return JsonResponse(json.loads(data), safe=False)


def updateOneSubject(request, id):
    obj = get_object_or_404(Subject, id=id)
    subject = SubjectForm(request.POST, instance=obj)
    if subject.is_valid():
        subject.save()
        return JsonResponse(subject.data)
    else:
        return JsonResponse(subject.errors, status=400)


def deleteOneSubject(request, id):
    obj = get_object_or_404(Subject, id=id)
    obj.delete()
    return JsonResponse({'status': 'success'})


def oneSubjectController(request, id):
    if request.method == 'GET':
        return getOneSubject(request, id)
    elif request.method == 'POST':
        return updateOneSubject(request, id)
    elif request.method == 'DELETE':
        return deleteOneSubject(request, id)
    else:
        return JsonResponse({'message:': 'method not allowed'}, status=405)
