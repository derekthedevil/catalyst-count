from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    year = models.PositiveIntegerField(default=2000)
    industry = models.TextField(default='UNKNOWN')
    size_range = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default='Unknown')
    linkedin_url = models.CharField(max_length=200)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()