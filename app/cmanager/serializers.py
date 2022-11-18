from rest_framework import serializers
from .models import WorkArrangement, Employee, TeamLeader, Team, TeamEmployee

class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class TeamLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLeader
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class TeamEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamEmployee
        fields = "__all__"
