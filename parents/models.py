from django.db import models

# Create your models here.


class Parent(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
