from django.urls import path
from .views import EmployeeAPIView, TeamLeaderAPIView, TeamAPIView, WarrangementAPIView, TemployeeAPIView

urlpatterns = [
    path('employee', EmployeeAPIView.as_view()),
    path('employee/<str:pk>', EmployeeAPIView.as_view()), # to capture our ids
    path('workarrangement', WarrangementAPIView.as_view()),
    path('workarrangement/<str:pk>', WarrangementAPIView.as_view()),
    path('teamleader', TeamLeaderAPIView.as_view()),
    path('teamleader/<str:pk>', TeamLeaderAPIView.as_view()),
    path('team', TeamAPIView.as_view()),
    path('team/<str:pk>', TeamAPIView.as_view()),
    path('teamemployee', TemployeeAPIView.as_view()),
    path('teamemployee/<str:pk>', TemployeeAPIView.as_view()),
]