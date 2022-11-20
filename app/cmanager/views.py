from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Person, WorkArrangement, Employee, Team
from .serializers import PersonSerializer, EmployeeSerializer, TeamSerializer, WorkArrangementSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet()):
    
    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

class WarrangementViewSet(viewsets.ModelViewSet()):
    
    def list(self, request):
        queryset = WorkArrangement.objects.all()
        serializer = WorkArrangementSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = WorkArrangement.objects.all()
        wa = get_object_or_404(queryset, pk=pk)
        serializer = WorkArrangementSerializer(wa)
        return Response(serializer.data)
    
class EmployeeViewSet(viewsets.ModelViewSet()):
    
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class TeamViewSet(viewsets.ModelViewSet()):
    
    def list(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)