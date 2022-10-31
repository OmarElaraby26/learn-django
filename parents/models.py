from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


is_valid_name_regex = RegexValidator(
    regex="^[A-Z][a-z]+$", message="name must be at least 3 letters and contain only lowercase letters except the first one must be uppercase")


class Parent(models.Model):

    firstname = models.CharField(
        max_length=32,  validators=[is_valid_name_regex])
    lastname = models.CharField(
        max_length=32,  validators=[is_valid_name_regex])
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
