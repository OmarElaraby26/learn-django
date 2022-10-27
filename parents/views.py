from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Parent
from .forms import ParentForm
import json
from django.core import serializers


def getAllParents(request):
    allParents = serializers.serialize('json', Parent.objects.all())
    return JsonResponse(json.loads(allParents), safe=False)


def createParent(request):
    newParent = ParentForm(request.POST)
    if newParent.is_valid():
        newParent.save()
        return JsonResponse(newParent.data, status=201)
    else:
        return JsonResponse(newParent.errors, status=409)


def parentsController(request):
    if request.method == 'GET':
        return getAllParents(request)
    if request.method == 'POST':
        return createParent(request)


def getOneParent(request, id):
    data = serializers.serialize('json', Parent.objects.all().filter(id=id))
    return JsonResponse(json.loads(data), safe=False)


def updateOneParent(request, id):
    obj = get_object_or_404(Parent, id=id)
    parent = ParentForm(request.POST, instance=obj)
    if parent.is_valid():
        parent.save()
        return JsonResponse(parent.data)
    else:
        return JsonResponse(parent.errors, status=400)


def deleteOneParent(request, id):
    obj = get_object_or_404(Parent, id=id)
    obj.delete()
    return JsonResponse({'status': 'success'})


def oneParentController(request, id):
    if request.method == 'GET':
        return getOneParent(request, id)
    elif request.method == 'POST':
        return updateOneParent(request, id)
    elif request.method == 'DELETE':
        return deleteOneParent(request, id)
    else:
        return JsonResponse({'message:': 'method not allowed'}, status=405)
