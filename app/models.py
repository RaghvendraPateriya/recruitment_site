from django.contrib.auth.models import User
from django.db import models


class SkillSet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SkillSet'


class UserDetail(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    QUALIFICATION_CHOICES = (
        ('btech', 'B Tech'),
        ('bsc', 'BSc (IT)'),
        ('mca', 'MCA'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=100)
    passing_year = models.IntegerField()
    percentage = models.IntegerField()
    company = models.CharField(max_length=100)
    ctc = models.IntegerField()
    experience = models.IntegerField()
    skills = models.ManyToManyField(SkillSet)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'UserDetail'
