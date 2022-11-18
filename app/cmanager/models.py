from django.db import models



#Work arrangement class, 4 types with percentage 
class WorkArrangement(models.Model):
    type = ( 
        ('40', 'Fulltime'),
        ('30', 'Part-time, 75%'),
        ('20', 'Part-time, 50%'),
        ('10', 'Part-time, 25%')
    )

# Employee model with name, id, team, hourly rate
class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hourlyRate = models.FloatField()
    workArrangement = models.ForeignKey(WorkArrangement, on_delete=models.CASCADE)
    def salary(self):
        return self.workArrangement * self.hourlyRate

#Team leader class inherits the Employee fields and adds the bonus for additional tasks
class TeamLeader(Employee):
    def salary(self):
        return (self.workArrangement * self.hourlyRate) * (11/10)

#Team class
class Team(models.Model):
    id = models.BigAutoField(primary_key=True)

class TeamEmployee(models.Model):
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    teamId = models.ForeignKey(Team, on_delete=models.CASCADE)