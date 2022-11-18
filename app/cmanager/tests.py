from django.test import TestCase
from .models import WorkArrangement, Employee, Team, TeamLeader, TeamEmployee
from django.utils import timezone
from django.core.urlresolvers import reverse
from whatever.forms import WhateverForm

# models test
class WarrangementTest(TestCase):

    def create_wa(self, title="only a test", body="yes, this is only a test"):
        return WorkArrangement.objects.create(title=title, body=body, created_at=timezone.now())

    def test_wa_creation(self):
        w = self.create_wa()
        self.assertTrue(isinstance(w, WorkArrangement))
        self.assertEqual(w.__unicode__(), w.title)

class EmployeeTest(TestCase):

    def create_employee(self, title="only a test", body="yes, this is only a test"):
        return Employee.objects.create(title=title, body=body, created_at=timezone.now())

    def test_employee_creation(self):
        w = self.create_employee()
        self.assertTrue(isinstance(w, Employee))
        self.assertEqual(w.__unicode__(), w.title)

class TeamTest(TestCase):

    def create_team(self, title="only a test", body="yes, this is only a test"):
        return Team.objects.create(title=title, body=body, created_at=timezone.now())

    def test_team_creation(self):
        w = self.create_team()
        self.assertTrue(isinstance(w, Team))
        self.assertEqual(w.__unicode__(), w.title)

class TeamLeaderTest(TestCase):

    def create_team_leader(self, title="only a test", body="yes, this is only a test"):
        return TeamLeader.objects.create(title=title, body=body, created_at=timezone.now())

    def test_team_leader_creation(self):
        w = self.create_team_leader()
        self.assertTrue(isinstance(w, Employee))
        self.assertEqual(w.__unicode__(), w.title)

class TeamEmployeeTest(TestCase):

    def create_team_employee(self, title="only a test", body="yes, this is only a test"):
        return TeamEmployee.objects.create(title=title, body=body, created_at=timezone.now())

    def test_team_employee_creation(self):
        w = self.create_employee()
        self.assertTrue(isinstance(w, TeamEmployee))
        self.assertEqual(w.__unicode__(), w.title)
