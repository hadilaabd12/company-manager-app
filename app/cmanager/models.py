from django.db import models

# Employee model with name, id, team, hourly rate
class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    hourlyRate = models.FloatField()
    workArrangement = models.ForeignKey(WorkArrangement, on_delete=models.CASCADE)
    def salary(self):
        return workArrangement * hourlyRate

class Team(models.Model):
    id = models.BigAutoField(primary_key=True)


class WorkArrangement(models.Model):
    type = ( 
        'Fulltime',
        'Part-time, 25%',
        'Part-time, 50%',
        'Part-time, 75%'
    )
