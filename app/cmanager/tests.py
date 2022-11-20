from django.test import TestCase
from .models import Person, WorkArrangement, Employee, Team
from django.utils import timezone


# models test
class PersonTest(TestCase):

    def create_wa(self, name="Person 1"):
        return Employee.objects.create(name=name, created_at=timezone.now())

    def test_wa_creation(self):
        w = self.create_wa(name="Person 1")
        self.assertTrue(isinstance(w, Person))
        self.assertEqual(w.__unicode__(), w.name)


class WarrangementTest(TestCase):

    def create_wa(self, type=40):
        return WorkArrangement.objects.create(
            type=type,
            created_at=timezone.now()
        )

    def test_wa_creation(self):
        wa = 40
        w = self.create_wa(wa)
        self.assertTrue(isinstance(w, WorkArrangement))
        self.assertEqual(w.__unicode__(), w.type)


class EmployeeTest(TestCase):

    workArrangement=WorkArrangement(type=40)
    WorkArrangement.save(workArrangement)
    def create_employee(
        self,
        name="Employee 1",
        hourly_rate=10,
        workArrangement=workArrangement, 
        created_at=timezone.now()):
            return Employee.objects.create(
                name=name,
                hourly_rate=hourly_rate,
                workArrangement=workArrangement,
                created_at=timezone.now()
            )

    def test_employee_creation(self):
        
        w = self.create_employee(
            name="Employee 1",
            hourly_rate=10,
            workArrangement=WorkArrangement(type=40)
        )
        self.assertTrue(isinstance(w, Employee))
        self.assertEqual(w.__unicode__(), w.name)


class TeamTest(TestCase):

    def create_team(self, type='Employee'):
        return Team.objects.create(type=type, created_at=timezone.now())

    def test_team_creation(self):
        w = self.create_team(type='Employee')
        self.assertTrue(isinstance(w, Team))
        self.assertEqual(w.__unicode__(), w.type)
