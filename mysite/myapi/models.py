from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename
             
