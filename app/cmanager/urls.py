from django.urls import path
from .views import PersonViewSet, EmployeeViewSet, WarrangementViewSet, TeamViewSet

urlpatterns = [
    path('person', PersonViewSet.as_view()),
    path('person/<str:pk>', PersonViewSet.as_view()),  # to capture our ids
    path('employee', EmployeeViewSet.as_view()),
    path('employee/<str:pk>', EmployeeViewSet.as_view()),
    path('workarrangement', WarrangementViewSet.as_view()),
    path('workarrangement/<str:pk>', WarrangementViewSet.as_view()),
    path('team', TeamViewSet.as_view()),
    path('team/<str:pk>', TeamViewSet.as_view()),
]
