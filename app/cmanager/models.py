from django.db import models


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


# Work arrangement class, 4 types with percentage
class WorkArrangement(models.Model):
    type = (
        ('40', 'Fulltime'),
        ('30', 'Part-time, 75%'),
        ('20', 'Part-time, 50%'),
        ('10', 'Part-time, 25%')
    )


# Employee model with name, id, team, hourly rate
class Employee(Person):
    idContract = models.BigAutoField(primary_key=True)
    hourly_rate = models.FloatField(default=0.00)
    workArrangement = models.ForeignKey(
        WorkArrangement,
        on_delete=models.CASCADE
    )
    isLead = models.BooleanField(default=False)

    def salary(self):
        if self.isLead:
            return (self.workArrangement * self.hourlyRate) * (11/10)
        else:
            return self.workArrangement * self.hourlyRate


# Team class
class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    members = models.ManyToManyField(Employee)
    type = (
        ('E', 'Employee'),
        ('L', 'Leader')
    )
