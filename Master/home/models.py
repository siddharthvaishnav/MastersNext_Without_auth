from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=255)
    course = models.JSONField(default=list, null=True)
    salary = models.IntegerField(null=True)
    graduation_rate = models.FloatField(null=True, default=0.0)
    cost_0_to_30k = models.IntegerField(null=True)
    cost_30_to_48k = models.IntegerField(null=True)
    cost_48_to_75k = models.IntegerField(null=True)
    cost_75_to_110k = models.IntegerField(null=True)
    cost_110k_plus = models.IntegerField(null=True)
    student_size = models.IntegerField(null=True)
    location = models.CharField(max_length=255)
    acceptance_rate = models.FloatField(null=True, default=0.0)
    grescore = models.FloatField(null=True, default=0.0)
    tuition = models.FloatField(null=True, default=0.0)
    link = models.CharField(max_length=255, default='#')
    toefl = models.IntegerField(null=True)
    ielts = models.IntegerField(null=True)
    cs_salary = models.IntegerField(null=True)
    datascience_salary = models.IntegerField(null=True)
    MBA_salary = models.IntegerField(null=True)
    logo = models.CharField(max_length=50, default='None')
    MBA_cost = models.IntegerField(null=True)
    CSE_cost = models.IntegerField(null=True)
    DataScience_cost = models.IntegerField(null=True)
    country = models.CharField(max_length=50, default='USA')
    hostelandmeals = models.IntegerField(null=True)
    transportation = models.IntegerField(null=True)
    personal = models.IntegerField(null=True)
    gate = models.IntegerField(null=True)
    cat = models.IntegerField(null=True)
    books = models.IntegerField(null=True)

    def to_dict(self):
        college = {
            "name": self.name,
            "course": self.course,
            "student_size": self.student_size,
            "location": self.location,
            "acceptance_rate": self.acceptance_rate,
            "grescore": self.grescore,
            "tuition": self.tuition,
            "link": self.link,
            "graduation_rate": self.graduation_rate,
            "median_salary": self.salary,
            "cost_0_to_30k": self.cost_0_to_30k,
            "cost_30_to_48k": self.cost_30_to_48k,
            "cost_48_to_75k": self.cost_48_to_75k,
            "cost_75_to_110k": self.cost_75_to_110k,
            "cost_110k_plus": self.cost_110k_plus,
            "cs_salary": self.cs_salary,
            "datascience_salary": self.datascience_salary,
            "MBA_salary": self.MBA_salary,
            "ielts": self.ielts,
            "toefl": self.toefl,
            "salary": self.salary,
            "logo": self.logo,
            "MBA_cost": self.MBA_cost,
            "CSE_cost": self.CSE_cost,
            "DataScience_cost": self.DataScience_cost,
            "country": self.country,
            "hostelandmeals": self.hostelandmeals,
            "transportation": self.transportation,
            "personal": self.personal,
            "gate": self.gate,
            "cat": self.cat,
            "books": self.books,


        }
        return college


class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default=None)
    amount = models.FloatField(max_length=255)
    deadline = models.CharField(max_length=50)
    link = models.CharField(max_length=250)

    def scholar_dict(self):
        scholarship = {
            "name": self.name,
            "desc": self.desc,
            "amount": self.amount,
            "deadline": self.deadline,
            "link": self.link
        }
        return scholarship
