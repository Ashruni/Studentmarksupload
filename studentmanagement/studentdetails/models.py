from django.db import models

# Create your models here.
class studentdetailmodel(models.Model):
    studentname=models.CharField(max_length=20)
    studentdob=models.DateField()
    Physicsmarks=models.IntegerField()
    Chemistrymarks=models.IntegerField()
    Mathsmarks=models.IntegerField()
    Computersciencemarks=models.IntegerField()


