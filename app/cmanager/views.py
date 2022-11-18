from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import WorkArrangement, Employee, Team, TeamLeader, TeamEmployee
from .serializers import EmployeeSerializer, TeamSerializer, TeamLeaderSerializer, WorkArrangementSerializer, TeamEmployeeSerializer
from rest_framework.response import Response

class WarrangementAPIView(APIView):
    # READ a single Work Arrangement
    def get_object(self, pk):
        try:
            return WorkArrangement.objects.get(pk=pk)
        except WorkArrangement.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = WorkArrangementSerializer(data)

        else:
            data = WorkArrangement.objects.all()
            serializer = WorkArrangementSerializer(data, many=True)

            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = WorkArrangementSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create WA in the DB
        serializer.save()

        # Return Response to User
        response = Response()
        response.data = {
            'message': 'WorkArrangement Created Successfully',
            'data': serializer.data
        }
        return response
    def put(self, request, pk=None, format=None):
        # Get the work arrangement to update
        wa_to_update = WorkArrangement.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = WorkArrangementSerializer(instance=wa_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Work Arrangement Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        wa_to_delete =  WorkArrangement.objects.get(pk=pk)

        # delete the work arrangement
        wa_to_delete.delete()

        return Response({
            'message': 'Work Arrangement Deleted Successfully'
        })

class EmployeeAPIView(APIView):
    # READ a single Employee
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = EmployeeSerializer(data)

        else:
            data = Employee.objects.all()
            serializer = EmployeeSerializer(data, many=True)

            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = EmployeeSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Employee in the DB
        serializer.save()

        # Return Response to User
        response = Response()
        response.data = {
            'message': 'Employee Created Successfully',
            'data': serializer.data
        }
        return response
    def put(self, request, pk=None, format=None):
        # Get the employee to update
        employee_to_update = Employee.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = EmployeeSerializer(instance=employee_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Employee Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        employee_to_delete =  Employee.objects.get(pk=pk)

        # delete the employee
        employee_to_delete.delete()

        return Response({
            'message': 'Employee Deleted Successfully'
        })


class TeamLeaderAPIView(APIView):
    # READ a single TeamLeader
    def get_object(self, pk):
        try:
            return TeamLeader.objects.get(pk=pk)
        except TeamLeader.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = TeamLeaderSerializer(data)

        else:
            data = TeamLeader.objects.all()
            serializer = TeamLeaderSerializer(data, many=True)

            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = TeamLeaderSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create TeamLeader in the DB
        serializer.save()

        # Return Response to User
        response = Response()
        response.data = {
            'message': 'TeamLeader Created Successfully',
            'data': serializer.data
        }
        return response
    def put(self, request, pk=None, format=None):
        # Get the team leader to update
        teamlead_to_update = TeamLeader.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = TeamLeaderSerializer(instance=teamlead_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'TeamLeader Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        teamlead_to_delete =  TeamLeader.objects.get(pk=pk)

        # delete the team leader
        teamlead_to_delete.delete()

        return Response({
            'message': 'TeamLeader Deleted Successfully'
        })
class TeamAPIView(APIView):
    # READ a single Team
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = TeamSerializer(data)

        else:
            data = Team.objects.all()
            serializer = TeamSerializer(data, many=True)

            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = TeamSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Team in the DB
        serializer.save()

        # Return Response to User
        response = Response()
        response.data = {
            'message': 'Team Created Successfully',
            'data': serializer.data
        }
        return response
    def put(self, request, pk=None, format=None):
        # Get the team to update
        team_to_update = Team.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = TeamSerializer(instance=team_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Team Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        team_to_delete =  Team.objects.get(pk=pk)

        # delete the team
        team_to_delete.delete()

        return Response({
            'message': 'Team Deleted Successfully'
        })

class TemployeeAPIView(APIView):
    # READ a single TeamEmployee
    def get_object(self, pk):
        try:
            return TeamEmployee.objects.get(pk=pk)
        except TeamEmployee.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = TeamEmployeeSerializer(data)

        else:
            data = TeamEmployee.objects.all()
            serializer = TeamEmployeeSerializer(data, many=True)

            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = TeamEmployeeSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create TeamEmployee in the DB
        serializer.save()

        # Return Response to User
        response = Response()
        response.data = {
            'message': 'TeamEmployee Created Successfully',
            'data': serializer.data
        }
        return response
    def put(self, request, pk=None, format=None):
        # Get the team employee to update
        te_to_update = TeamEmployee.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = TeamEmployeeSerializer(instance=te_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'TeamEmployee Updated Successfully',
            'data': serializer.data
        }

        return response
    def delete(self, request, pk, format=None):
        te_to_delete =  TeamEmployee.objects.get(pk=pk)

        # delete the TeamEmployee
        te_to_delete.delete()

        return Response({
            'message': 'TeamEmployee Deleted Successfully'
        })