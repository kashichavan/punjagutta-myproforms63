from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    ename=models.CharField(max_length=25)
    eage=models.IntegerField()
    email=models.EmailField()
    sal=models.FloatField()

