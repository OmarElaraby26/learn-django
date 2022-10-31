from parents.serializers import ParentSerializer
from .models import Parent
from rest_framework import generics


class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
