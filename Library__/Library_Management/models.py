from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    pages=models.PositiveIntegerField()
    publish_date=models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    roll_no=models.PositiveIntegerField()
   
    def __str__ (self):
        return self.first_name + ' ' + self.last_name