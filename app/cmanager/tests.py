from django.test import TestCase
from .models import WorkArrangement, Employee, Team, TeamLeader, TeamEmployee
from django.utils import timezone


# models test
class PersonTest(TestCase):

    def create_wa(self, name="Person 1"):
        return Employee.objects.create(type=type, created_at=timezone.now())

    def test_wa_creation(self):
        w = self.create_wa()
        self.assertTrue(isinstance(w, Employee))
        self.assertEqual(w.__unicode__(), w.name)


class WarrangementTest(TestCase):

    def create_wa(self, type='40'):
        return WorkArrangement.objects.create(
            type=type,
            created_at=timezone.now()
        )

    def test_wa_creation(self):
        w = self.create_wa()
        self.assertTrue(isinstance(w, WorkArrangement))
        self.assertEqual(w.__unicode__(), w.type)


class EmployeeTest(TestCase):

    def create_employee(self, name="Employee 1", hourly_rate=10):
        return Employee.objects.create(
            name=name,
            hourly_rate=hourly_rate,
            created_at=timezone.now()
        )

    def test_employee_creation(self):
        w = self.create_employee()
        self.assertTrue(isinstance(w, Employee))
        self.assertEqual(w.__unicode__(), w.name)


class TeamTest(TestCase):

    def create_team(self, type='E'):
        return Team.objects.create(type=type, created_at=timezone.now())

    def test_team_creation(self):
        w = self.create_team()
        self.assertTrue(isinstance(w, Team))
        self.assertEqual(w.__unicode__(), w.title)
