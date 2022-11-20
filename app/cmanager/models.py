import datetime
from django.db import models


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=True)

    def create(self, name, created_at=None):
        self.name = name
        if created_at is None:
            self.created_at = datetime.utcnow()
        else:
            self.created_time = created_at


# Work arrangement class, 4 types with percentage
class WorkArrangement(models.Model):
    id = models.BigAutoField(primary_key=True)
    ft = 40
    pt_75 = 30
    pt_50 = 20
    pt_25 = 10
    work_type = (
        (ft, 'Fulltime'),
        (pt_75, 'Part-time, 75%'),
        (pt_50, 'Part-time, 50%'),
        (pt_25, 'Part-time, 25%')
    )
    type = models.IntegerField(
        choices=work_type,
        default=ft
    )
    created_at = models.DateTimeField(null=True)

    def create(self, type, created_at=None):
        self.type = type
        if created_at is None:
            self.created_at = datetime.utcnow()
        else:
            self.created_at = created_at

    def __unicode__(self):
        return self.type


# Employee model with name, id, team, hourly rate
class Employee(Person):
    idContract = models.BigAutoField(primary_key=True)
    hourly_rate = models.FloatField(default=0.00, null=True)
    workArrangement = models.ForeignKey(
        WorkArrangement,
        on_delete=models.CASCADE,
        null=True
    )
    isLead = models.BooleanField(default=False, null=True)

    def create(self, name, hourly_rate, created_at=None):
        self.name = name
        self.hourly_rate = hourly_rate
        # self.workArrangement = workArrangement
        if created_at is None:
            self.created_at = datetime.utcnow()
        else:
            self.created_at = created_at

    def salary(self):
        if self.isLead:
            return (self.workArrangement * self.hourlyRate) * (11/10)
        else:
            return self.workArrangement * self.hourlyRate

    def __unicode__(self):
        return self.name


# Team class
class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    members = models.ManyToManyField(Employee)
    team_type = (
        ('E', 'Employee'),
        ('L', 'Leader')
    )
    type = models.CharField(
        max_length=2,
        choices=team_type,
        default='Employee'
    )
    created_at = models.DateTimeField(null=True)

    def create(self, type, created_at=None):
        self.type = type
        if created_at is None:
            self.created_at = datetime.utcnow()
        else:
            self.created_time = created_at

    def __unicode__(self):
        return self.type
