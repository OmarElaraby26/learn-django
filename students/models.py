
from django.db import models

from parents.models import Parent
from subjects.models import Subject

# Create your models here.


def validateName(name):
    if not all(x.isalpha for x in name):
        return False
    if not all(x.islower for x in name[1::]):
        return False
    return name[0].isupper()


class Student(models.Model):
    firstname = models.CharField(max_length=32, validators=[validateName])
    lastname = models.CharField(max_length=32, validators=[validateName])
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    year = models.PositiveIntegerField()

    parent = models.ForeignKey(
        Parent, related_name='parents', on_delete=models.SET_NULL, null=True, blank=True)

    subjects = models.ManyToManyField(
        Subject, related_name='subjects', blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        unique_together = [['firstname', 'lastname']]

        indexes = [models.Index(
            fields=['firstname', 'lastname'], name='first_last_name_index')]

        constraints = [
            models.CheckConstraint(
                name='age greater than 15', check=models.Q(age__gt=15))
        ]
