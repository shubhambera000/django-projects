from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=40)
    adress = models.CharField(max_length=250)
    Email_id = models.EmailField(blank=True, default='')


class College(models.Model):
    b = models.ForeignKey(Details, on_delete=models.CASCADE)
    CGPA = models.IntegerField()
    Roll_no = models.CharField(max_length=30)
