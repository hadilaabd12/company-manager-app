from .models import Person, WorkArrangement, Employee, Team
from .serializers import PersonSerializer, EmployeeSerializer, TeamSerializer, WorkArrangementSerializer
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet()):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class WarrangementViewSet(viewsets.ModelViewSet()):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer
    
class EmployeeViewSet(viewsets.ModelViewSet()):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TeamViewSet(viewsets.ModelViewSet()):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer